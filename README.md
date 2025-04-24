# Murray-NCAR-GVP
This set of notebooks and folders is the code and data that is associated with the publication: 

**Evaluating CAM-chem modeled atmospheric wet deposition with observed long-term records** 

**Primary author**: Desneiges (Deni) Murray

**Co-authors**: Rebecca R. Buchholz, Louisa K. Emmons, Shawn Honomichl, Wenfu Tang, Simone Tilmes, Mary Barth, and Adam S. Wymore

Submitted for review to Journal of Geophysical Research: Atmospheres


| File                                                                                  | Description                                                                                                                               |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `Compilation or base analyses/Timeseries_creation.ipynb`                                      | Code to convert daily modeled .nc files to a single timeseries file                                                                       |
| `Compilation or base analyses/Precip_SO4_NO3_NH4_DailyOutputAnalyses.ipynb`                   | Code to pair modeled timeseries data with observed timeseries data for precip, SO4, NO3, NH4, and NH3                                      |
| `Compilation or base analyses/BC_SOA_POM_wetdep_DailyOutputAnalyses.ipynb`                    | Code to pair modeled timeseries data with observed timeseries data for precip and DOC                                                     |
| `Final_Model_Comparisons.ipynb`                                                               | Code to read in raw paired model-observed datasets and clean based on precipitation error; includes Figure 1 error histograms and Figure S1 |
| `MUSICA Analyses/MUSICA timeseries creation.ipynb`                                           | Code to convert daily modeled .nc files to a single timeseries file from the MUSICA output                                                |
| `MUSICA Analyses/MUSICA_clean and merge timeseries.ipynb`                                     | Code to clean modeled and observed data and merge together for MUSICA output                                                               |
| `Map_ModObs_Raw.ipynb`                                                                        | Code for creating Figure 1                                                                                                                 |
| `Timeseries_plotting.ipynb`                                                                   | Code for creating Figure 2 and running regression and seasonality statistics                                                              |
| `Concentration_Binned_Plot.ipynb`                                                             | Code for creating Figure 3                                                                                                                 |
| `Model Metrics_plotting.ipynb`                                                                | Code for running spatial statistics (KGE) and creating Figure S3                                                                           |
| `KGE_Map_Plotting.py`                                                                         | Code for creating Figure 4                                                                                                                 |
| `MUSICA Analyses/MUSICA final plots and analyses.ipynb`                                       | Code for creating Figure 5 and running stats                                                                                                |
| `Emission trends.ipynb`                                                                       | Code for creating Figure S2                                                                                                                |
| `RR Ann Avg maps.ipynb`                                                                       | Code for creating Figure S4                                                                                                                |
| `Solute proportion plots.ipynb`                                                               | Code for creating Figure S5                                                                                                                |
| `MUSICA Analyses/RR Global CONUS comparison.ipynb`                                            | Code for creating Figure S6                                                                                                                |
| `RR Glob Obs timeseries plotting.ipynb`                                                       | Code for creating Figure S7                                                                                                                |
| `Data outputs for publication/MUSICA_nadp_merged_gridded_daily_timeseries.nc`                 | Data output for selecting MUSICA cells that correspond with NADP sites                                                                     |
| `Data outputs for publication/Clean and filtered RR Glob Obs timeseries.csv`                  | Data output of paired wet‐deposition and precipitation data for MUSICA, uniform grid, and observed data after precip filter               |
| `Data outputs for publication/Precip Filtered Cleaned Paired Modeled Observed Timeseries FINAL.csv` | Data output of paired wet‐deposition and precipitation data for uniform grid and observed data after precip filter                      |
| `Data outputs for publication/DOC_wetdep_compiled.csv`                                        | Observed DOC data compiled                                                                                                                |
| `Data outputs for publication/PREC_DOC_BC_Timeseries.SamplingInt_Summed_pairedNADPsites.csv` | Raw paired modeled and observed data for DOC and precip, summed across composite sampling intervals                                        |
| `Data outputs for publication/PREC_SO4_NO3_NH4_NH3_Timeseries.SamplingInt_Summed_pairedNADPsites.csv` | Raw paired modeled and observed data for SO4, NO3, NH4, NH3, and precip, summed across composite sampling intervals                        |

**Key points**
1.	CAM-chem captures general seasonal to long-term patterns but overestimates NO3⁻ and underestimates SO42⁻, NH4⁺, and DOC deposition fluxes.
2.	Wet deposition fluxes are consistent between the uniform grid and the regionally refined model resolution versions.
3.	Validating modeled wet deposition is crucial for applying fluxes to biogeochemical modules within the dynamic earth model framework.
   
**Abstract**

Accurate modeling of carbon, nitrogen, and sulfur wet deposition (i.e., through rain, snow, or cloud-water) flux is important for characterizing and quantifying the role of deposition in global biogeochemical cycles. The simulation of wet deposition of solutes in the Community Atmosphere Model version 6 with Chemistry (CAM-chem) has had limited previous evaluation leaving an opportunity to determine its accuracy in simulating precipitation rates and chemistry. Here, we assessed the accuracy of 1° resolution CAM-chem outputs of wet deposition over the contiguous U.S. (CONUS) from 2002-2022, comparing model outputs for observed equivalents of sulfate (SO42-), ammonium (NH4+), nitrate (NO3-), and dissolved organic carbon (DOC) wet deposition with long-term records collected at hundreds of stations across CONUS. After evaluating the temporal, spatial, and quantile differences between modeled and observed wet deposition fluxes, we find the model captures long-term and seasonal patterns but consistently overestimates NO3-, while underestimating SO₄2-, NH₄+, and DOC wet deposition fluxes. Model-measurement agreement improved at higher deposition flux quantiles and site-specific alignment was strongest for NO3-, and moderate for SO42- and NH4+. Low model-measurement agreement for DOC comparisons is likely due to focusing on aerosol contributions. Higher resolution model simulations (~14 km) resulted in equivalent comparisons as the 1° model, suggesting that wet deposition processes are represented consistently across different model simulations and spatial resolution is not the main driver of inaccuracies of model deposition. Benchmarking modeled deposition outputs is crucial for evaluating CAM-chem's performance and its utility in understanding landscape drivers of deposition chemistry within Earth system models. 

