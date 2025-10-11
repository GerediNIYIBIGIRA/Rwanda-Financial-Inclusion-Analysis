import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Rwanda Financial Inclusion Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

    
#return demographics, financial_services
demographics=pd.read_csv("demographics.csv")
financial_services=pd.read_csv("financial_services.csv")    

@st.cache_data
def prepare_analysis_data():
    """Prepare merged dataset for analysis"""
    df = demographics.merge(financial_services, on='respondent_id', how='inner')
    
    # Create derived variables
    df['any_formal_service'] = (
        (df['has_bank_account'] == 1) | 
        (df['uses_mobile_money'] == 1) | 
        (df['has_savings'] == 1)
    )
    df['income_quintile'] = pd.qcut(df['monthly_income_rwf'], q=5, labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])
    
    return df

def main():
    # Header
    st.markdown('<h1 class="main-header">Rwanda Financial Inclusion Analysis</h1>', unsafe_allow_html=True)
    st.markdown("**Interactive Dashboard for Financial Inclusion Patterns in Rwanda**")
    st.markdown("---")
    
    # Load data
    df = prepare_analysis_data()
    
    # Sidebar for controls
    st.sidebar.header("Dashboard Controls")
    
    # Analysis selection
    analysis_type = st.sidebar.selectbox(
        "Select Analysis View:",
        ["Executive Overview", "Demographic Analysis", "Provincial Analysis", "Service Usage", "Market Segments", "Policy Insights"]
    )
    
    # Filters
    st.sidebar.subheader("Filters")
    selected_provinces = st.sidebar.multiselect(
        "Select Provinces:",
        options=df['province'].unique(),
        default=df['province'].unique()
    )
    
    urban_rural_filter = st.sidebar.selectbox(
        "Urban/Rural Filter:",
        options=['All', 'Urban', 'Rural'],
        index=0
    )
    # --- Sidebar Personal Information ---
    st.sidebar.title("Developer Information")
    st.sidebar.markdown("""
    **Name:** Geredi Niyibigira  
    **Role:** AI Consultant – Malaria Eradication Project  
    **Organization:** [Charis Unmanned Aerial Solution (UAS)](https://charisuas.com/)   
    **Email:** niygeredi@gmail.com | geredi.niyibigira@charisuas.com
    """)

    
    # Apply filters
    filtered_df = df[df['province'].isin(selected_provinces)]
    if urban_rural_filter != 'All':
        filtered_df = filtered_df[filtered_df['urban_rural'] == urban_rural_filter]
    
    # Main dashboard content
    if analysis_type == "Executive Overview":
        show_executive_overview(filtered_df)
    elif analysis_type == "Demographic Analysis":
        show_demographic_analysis(filtered_df)
    elif analysis_type == "Provincial Analysis":
        show_provincial_analysis(filtered_df)
    elif analysis_type == "Service Usage":
        show_service_usage(filtered_df)
    elif analysis_type == "Market Segments":
        show_market_segments(filtered_df)
    elif analysis_type == "Policy Insights":
        show_policy_insights(filtered_df)

def show_executive_overview(df):
    st.header("Executive Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        formal_inclusion = df['any_formal_service'].mean()
        st.metric(
            "Formal Financial Inclusion", 
            f"{formal_inclusion:.1%}",
            delta=f"Target: 75%"
        )
    
    with col2:
        mobile_money = df['uses_mobile_money'].mean()
        st.metric(
            "Mobile Money Usage", 
            f"{mobile_money:.1%}",
            delta=f"vs Banking: +{(mobile_money - df['has_bank_account'].mean()):.1%}"
        )
    
    with col3:
        avg_literacy = df['financial_literacy_score'].mean()
        st.metric(
            "Avg Financial Literacy", 
            f"{avg_literacy:.1f}/10",
            delta="Target: 8.0"
        )
    
    with col4:
        excluded_count = len(df[df['any_formal_service'] == False])
        st.metric(
            "Financially Excluded", 
            f"{excluded_count:,}",
            delta=f"{excluded_count/len(df):.1%} of population"
        )
    
    # Main visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # Service adoption rates
        services = ['Bank Account', 'Mobile Money', 'Savings', 'Loans', 'Insurance']
        rates = [
            df['has_bank_account'].mean(),
            df['uses_mobile_money'].mean(),
            df['has_savings'].mean(),
            df['has_loan'].mean(),
            df['uses_insurance'].mean()
        ]
        
        fig = px.bar(
            x=services, 
            y=rates,
            title="Financial Service Adoption Rates",
            labels={'x': 'Service Type', 'y': 'Adoption Rate'}
        )
        fig.update_traces(texttemplate='%{y:.1%}', textposition='outside')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Urban vs Rural comparison
        comparison_data = df.groupby('urban_rural').agg({
            'has_bank_account': 'mean',
            'uses_mobile_money': 'mean',
            'any_formal_service': 'mean'
        }).reset_index()
        
        fig = px.bar(
            comparison_data,
            x='urban_rural',
            y=['has_bank_account', 'uses_mobile_money', 'any_formal_service'],
            title="Urban vs Rural Financial Inclusion",
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)

def show_demographic_analysis(df):
    st.header("👥 Demographic Analysis")
    
    # Analysis by education
    st.subheader("Financial Inclusion by Education Level")
    edu_analysis = df.groupby('education').agg({
        'any_formal_service': 'mean',
        'financial_literacy_score': 'mean',
        'monthly_income_rwf': 'mean'
    }).reset_index()
    
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=('Inclusion Rate', 'Financial Literacy', 'Average Income')
    )
    
    fig.add_trace(
        go.Bar(x=edu_analysis['education'], y=edu_analysis['any_formal_service'], name='Inclusion Rate'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=edu_analysis['education'], y=edu_analysis['financial_literacy_score'], name='Literacy Score'),
        row=1, col=2
    )
    
    fig.add_trace(
        go.Bar(x=edu_analysis['education'], y=edu_analysis['monthly_income_rwf'], name='Income (RWF)'),
        row=1, col=3
    )
    
    fig.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Age analysis
    st.subheader("Financial Services by Age Group")
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 45, 55, 100], 
                           labels=['18-25', '26-35', '36-45', '46-55', '56+'])
    
    age_analysis = df.groupby('age_group').agg({
        'uses_mobile_money': 'mean',
        'has_bank_account': 'mean'
    }).reset_index()
    
    fig = px.line(
        age_analysis,
        x='age_group',
        y=['uses_mobile_money', 'has_bank_account'],
        title="Service Adoption by Age Group"
    )
    st.plotly_chart(fig, use_container_width=True)

def show_provincial_analysis(df):
    st.header("🗺️ Provincial Analysis")
    
    # Provincial comparison
    province_stats = df.groupby('province').agg({
        'any_formal_service': 'mean',
        'uses_mobile_money': 'mean',
        'has_bank_account': 'mean',
        'monthly_income_rwf': 'mean',
        'financial_literacy_score': 'mean'
    }).reset_index()
    
    # Sort by inclusion rate
    province_stats = province_stats.sort_values('any_formal_service', ascending=True)
    
    fig = px.bar(
        province_stats,
        x='any_formal_service',
        y='province',
        orientation='h',
        title="Financial Inclusion Rate by Province",
        text='any_formal_service'
    )
    fig.update_traces(texttemplate='%{text:.1%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed provincial table
    st.subheader("Detailed Provincial Statistics")
    province_display = province_stats.copy()
    province_display['any_formal_service'] = province_display['any_formal_service'].map('{:.1%}'.format)
    province_display['uses_mobile_money'] = province_display['uses_mobile_money'].map('{:.1%}'.format)
    province_display['has_bank_account'] = province_display['has_bank_account'].map('{:.1%}'.format)
    province_display['monthly_income_rwf'] = province_display['monthly_income_rwf'].map('{:,.0f}'.format)
    province_display['financial_literacy_score'] = province_display['financial_literacy_score'].map('{:.1f}'.format)
    
    province_display.columns = ['Province', 'Inclusion Rate', 'Mobile Money', 'Banking', 'Avg Income (RWF)', 'Literacy Score']
    st.dataframe(province_display, use_container_width=True)

def show_service_usage(df):
    st.header("💳 Financial Service Usage Patterns")
    
    # Service combination analysis
    df['service_count'] = (
        df['has_bank_account'] + df['uses_mobile_money'] + 
        df['has_savings'] + df['has_loan'] + df['uses_insurance']
    )
    
    service_dist = df['service_count'].value_counts().sort_index()
    
    fig = px.bar(
        x=service_dist.index,
        y=service_dist.values,
        title="Distribution of Number of Services Used",
        labels={'x': 'Number of Services', 'y': 'Number of People'}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Income vs service usage
    st.subheader("Service Usage by Income Level")
    income_service = df.groupby('income_quintile').agg({
        'has_bank_account': 'mean',
        'uses_mobile_money': 'mean',
        'has_savings': 'mean',
        'service_count': 'mean'
    }).reset_index()
    
    fig = px.line(
        income_service,
        x='income_quintile',
        y=['has_bank_account', 'uses_mobile_money', 'has_savings'],
        title="Service Adoption by Income Quintile"
    )
    st.plotly_chart(fig, use_container_width=True)

def show_market_segments(df):
    st.header("Market Segmentation")
    
    # Define segments
    segments = {}
    
    # Digital Champions (mobile + bank)
    digital_champions = df[(df['uses_mobile_money'] == 1) & (df['has_bank_account'] == 1)]
    segments['Digital Champions'] = len(digital_champions)
    
    # Mobile-only users
    mobile_only = df[(df['uses_mobile_money'] == 1) & (df['has_bank_account'] == 0)]
    segments['Mobile-Only Users'] = len(mobile_only)
    
    # Traditional banking only
    bank_only = df[(df['has_bank_account'] == 1) & (df['uses_mobile_money'] == 0)]
    segments['Traditional Banking'] = len(bank_only)
    
    # Financially excluded
    excluded = df[(df['has_bank_account'] == 0) & (df['uses_mobile_money'] == 0)]
    segments['Financially Excluded'] = len(excluded)
    
    # Pie chart
    fig = px.pie(
        values=list(segments.values()),
        names=list(segments.keys()),
        title="Market Segmentation"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Segment characteristics
    st.subheader("Segment Characteristics")
    segment_data = []
    
    for segment_name, segment_df in [
        ('Digital Champions', digital_champions),
        ('Mobile-Only Users', mobile_only),
        ('Traditional Banking', bank_only),
        ('Financially Excluded', excluded)
    ]:
        if len(segment_df) > 0:
            segment_data.append({
                'Segment': segment_name,
                'Size': len(segment_df),
                'Percentage': f"{len(segment_df)/len(df):.1%}",
                'Avg Income': f"{segment_df['monthly_income_rwf'].mean():,.0f}",
                'Urban %': f"{(segment_df['urban_rural'] == 'Urban').mean():.1%}",
                'Avg Literacy': f"{segment_df['financial_literacy_score'].mean():.1f}"
            })
    
    st.dataframe(pd.DataFrame(segment_data), use_container_width=True)

def show_policy_insights(df):
    st.header("Policy Insights & Recommendations")
    
    # Key findings
    st.subheader("Key Findings")
    
    urban_inclusion = df[df['urban_rural'] == 'Urban']['any_formal_service'].mean()
    rural_inclusion = df[df['urban_rural'] == 'Rural']['any_formal_service'].mean()
    urban_rural_gap = urban_inclusion - rural_inclusion
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"""
        **Urban-Rural Gap**: {urban_rural_gap:.1%}
        
        Urban areas show significantly higher financial inclusion rates. 
        This represents approximately {len(df[(df['urban_rural'] == 'Rural') & (df['any_formal_service'] == False)]):,} 
        excluded rural residents.
        """)
    
    with col2:
        mobile_advantage = df['uses_mobile_money'].mean() - df['has_bank_account'].mean()
        st.info(f"""
        **Mobile Money Advantage**: +{mobile_advantage:.1%}
        
        Mobile money adoption significantly exceeds traditional banking,
        suggesting digital-first strategies may be more effective.
        """)
    
    # Policy recommendations
    st.subheader("Strategic Recommendations")
    
    recommendations = [
        {
            "title": "Rural Mobile Money Agent Expansion",
            "priority": "HIGH",
            "description": "Expand mobile money agent networks in rural areas to bridge the urban-rural inclusion gap.",
            "target": f"{len(df[(df['urban_rural'] == 'Rural') & (df['any_formal_service'] == False)]):,} rural residents",
            "impact": "Could increase national inclusion by 8-12%"
        },
        {
            "title": "Financial Literacy Programs",
            "priority": "HIGH", 
            "description": "Implement targeted financial education for low-education demographics.",
            "target": f"{len(df[df['financial_literacy_score'] < 5]):,} individuals with low financial literacy",
            "impact": "Could improve literacy scores by 2-3 points"
        },
        {
            "title": "Digital-First Service Strategy",
            "priority": "MEDIUM",
            "description": "Prioritize mobile-based financial services over traditional banking infrastructure.",
            "target": f"{len(df[df['uses_mobile_money'] == 0]):,} non-mobile money users",
            "impact": "More cost-effective reach than traditional banking"
        }
    ]
    
    for i, rec in enumerate(recommendations, 1):
        priority_color = "🔴" if rec["priority"] == "HIGH" else "🟡"
        st.markdown(f"""
        **{i}. {rec['title']}** {priority_color}
        
        *{rec['description']}*
        
        - **Target Population**: {rec['target']}
        - **Expected Impact**: {rec['impact']}
        
        ---
        """)

if __name__ == "__main__":
    main()
