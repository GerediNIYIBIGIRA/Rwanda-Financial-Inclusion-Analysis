# Rwanda Financial Inclusion Analysis

A comprehensive data science project analyzing financial inclusion patterns in Rwanda, featuring interactive dashboards, market segmentation, and policy recommendations.

## Project Overview

This project provides deep insights into Rwanda's financial services landscape through data analysis of demographic patterns, service adoption rates, and barriers to financial inclusion. The analysis generates actionable policy recommendations for improving financial access across different population segments.

### Key Features

- **Interactive Web Dashboard**: Real-time data exploration and visualization
- **Market Segmentation**: Identification of distinct user groups and their characteristics  
- **Policy Insights**: Data-driven recommendations for financial inclusion strategies
- **Comprehensive Analysis**: Demographics, geographic, and behavioral patterns
- **SQL Analytics**: Advanced database queries for business intelligence

## Live Demo

- **Interactive Dashboard**: https://rwanda-financial-inclusion-analysis-ir76xdnlbyz9o8e7yeztnx.streamlit.app/
- **Jupyter Notebook**: https://github.com/GerediNIYIBIGIRA/Rwanda-Financial-Inclusion-Analysis

## 🔍 Key Findings

- **Financial Inclusion Rate**: 67.3% of Rwandans have access to formal financial services
- **Digital Advantage**: Mobile money adoption (80%) significantly exceeds traditional banking (60%)
- **Rural-Urban Gap**: 23% higher inclusion rates in urban areas
- **Education Impact**: Tertiary education increases inclusion probability by 31%

## Project Structure

```
rwanda-financial-inclusion/
│
├── data/
│   ├── demographics.csv          # Demographic survey data
│   └── financial_services.csv    # Financial service usage data
│
├── src/
│   ├── streamlit_app.py          # Interactive web dashboard
│   ├── data_analysis.py          # Core analysis functions
│   ├── visualization.py          # Chart and graph generation
│   └── policy_recommendations.py # Policy insight generation
│
├── notebooks/
│   └── financial_inclusion_analysis.ipynb  # Jupyter notebook version
│
├── outputs/
│   ├── executive_summary.txt     # Key findings summary
│   ├── dashboard_charts.png      # Static visualizations
│   └── policy_report.pdf         # Detailed recommendations
│
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── LICENSE                       # MIT License
```

## Quick Start

### Option 1: Interactive Web App

Visit the live dashboard: [Your Streamlit URL]

### Option 2: Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rwanda-financial-inclusion.git
   cd rwanda-financial-inclusion
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run src/streamlit_app.py
   ```

4. **Open browser** to `http://localhost:8501`

### Option 3: Jupyter Notebook

1. Open the Colab notebook: [Your Colab Link]
2. Run all cells to reproduce the analysis
3. Modify parameters to explore different scenarios

## Analysis Components

### 1. Data Processing Pipeline
- Data quality assessment and cleaning
- Missing value imputation strategies
- Outlier detection and handling
- Feature engineering and transformation

### 2. Exploratory Data Analysis
- Demographic distribution analysis
- Financial service adoption patterns
- Geographic and socioeconomic correlations
- Income and education impact assessment

### 3. Market Segmentation
- **Digital Champions** (20.1%): Full digital adoption
- **Mobile-Only Users** (35.7%): Mobile money focused
- **Traditional Banking** (11.5%): Bank-centric users
- **Financially Excluded** (32.7%): No formal services

### 4. Policy Recommendations
- Rural mobile money agent expansion
- Financial literacy enhancement programs
- Digital-first service strategies
- Cross-selling optimization initiatives

## Technical Implementation

### Technologies Used
- **Python**: Core analysis and processing
- **Pandas/NumPy**: Data manipulation and calculations
- **Plotly/Matplotlib**: Interactive and static visualizations
- **Streamlit**: Web application framework
- **SQLite**: Database queries and analytics
- **Seaborn**: Statistical data visualization

### Data Sources
- Synthetic demographic survey data (n=1,000)
- Financial service usage indicators
- Geographic and socioeconomic variables
- Financial literacy assessment scores

*Note: This project uses synthetic data for demonstration purposes. Real implementation would integrate with official survey data from institutions like NISR (National Institute of Statistics Rwanda).*

## Key Visualizations

The dashboard includes:

1. **Executive KPI Dashboard**: High-level inclusion metrics
2. **Geographic Analysis**: Province-by-province breakdowns
3. **Demographic Patterns**: Age, education, and gender analysis
4. **Service Usage Trends**: Adoption patterns across different services
5. **Market Segmentation**: Customer group characteristics
6. **Policy Impact Modeling**: Projected outcomes of interventions

## Business Impact

### For Policymakers
- Evidence-based policy recommendations
- Target population identification
- Resource allocation optimization
- Progress tracking mechanisms

### For Financial Institutions
- Market opportunity assessment
- Customer segmentation insights
- Product development guidance
- Risk assessment frameworks

### For Development Organizations
- Program effectiveness evaluation
- Impact measurement tools
- Stakeholder communication materials
- Grant application support

## Usage Examples

### Exploring Provincial Differences
```python
# Filter data for specific provinces
provinces = ['Kigali', 'Eastern']
filtered_analysis = analyze_by_province(data, provinces)
```

### Custom Market Segmentation
```python
# Create custom segments based on service usage
segments = create_market_segments(
    mobile_threshold=0.8,
    banking_threshold=0.6
)
```

### Policy Impact Simulation
```python
# Model impact of rural agent expansion
impact = simulate_rural_expansion(
    agent_increase=0.25,
    target_provinces=['Northern', 'Western']
)
```

## Updates and Maintenance

This project is actively maintained. Recent updates include:

- **v1.2**: Added predictive modeling capabilities
- **v1.1**: Enhanced mobile responsiveness
- **v1.0**: Initial dashboard release

## Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Areas for Contribution
- Additional data sources integration
- Advanced machine learning models
- Mobile app development
- Translation to Kinyarwanda

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Project Author**: Geredi Niyibigira
- Email: [ngeredi@alumni.cmu.edu/niygeredi@gmail.com]
- LinkedIn: www.linkedin.com/in/niyibigira-geredi-a880111a7
- Portfolio: https://gerediniyibigira-portfolio.netlify.app/

## Acknowledgments

- Rwanda's National Institute of Statistics for methodology guidance
- Financial sector development organizations for insights
- Open source community for tools and libraries

## References and Further Reading

1. [Rwanda Vision 2050 - Financial Inclusion Goals]
2. [Mobile Money Impact Studies in East Africa]
3. [World Bank Financial Inclusion Database]
4. [Cenfri Financial Inclusion Research]

---

**If you find this project useful, please consider giving it a star on GitHub!**

---

*Last updated: 02/09/2025*
*Dataset: Synthetic data for demonstration (1,000 samples)*
*Status: Active development*