This example builds a standalone APECSS code for an ultrasound-driven bubble.

#### Lipid-coated microbubble (simple)
This example simulates a lipid-coated microbubble using the Rayleigh-Plesset model including acoustic radiation damping. The lipid-monolayer coating is modelled using the Marmottant model. Using [lipidcoated_simple.apecss](lipidcoated_simple.apecss) with ````./build/ultrasound_apecss -options lipidcoated_simple.apecss -freq 2.9e6 -amp 130e3 -tend 2e-6````, this example reproduces Figure 5b of [Marmottant et al., _Journal of the Acoustical Society of America_ 118 (2005), 3499](https://doi.org/10.1121/1.2109427). 

#### Lipid-coated microbubble (with emissions)
This example simulated a lipid-coated microbubble using the Gilmore model and records its acoustic emissions based on the Kirkwood-Bethe hypothesis. The lipid-monolayer coating is modeled using the Marmottant-Gompertz model and the bubble is assumed to contain sulfur hexafluoride (SF6). Using [lipidcoated_emissions.apecss](lipidcoated_emissions.apecss) with ````./build/ultrasound_apecss -options lipidcoated_emissions.apecss -tend 11e-6 -freq 1e6 -amp 600e3````, a bubble excited by ultrasound with a frequency of 1 MHz and a pressure amplitude of 600 kPa is simulated. This example reproduces the case studied in Section IV.D of [Denner & Schenke, _Physics of Fluids_ 35 (2023), 012114](https://doi.org/10.1063/5.0131930), although the sock treatment has since then been improved and now predicts slightly higher pressure and velocity amplitudes then in the PoF paper.

#### Sonoluminescence (with emissions)
Using [sonolumin_emissions.apess](sonolum_emissions.apecss) with ````./build/ultrasound_apecss -options sonolum_emissions.apecss -tend 40e-6 -freq 23.5e3 -amp 145e3````, this example reproduces the argon bubble studied by [Holzfuss, _Proc. R. Soc. A: Math. Phys. Eng. Sci._ 466 (2010), 1829](https://doi.org/10.1098/rspa.2009.0594) in the context of sonoluminesence. The acoustic emissions at _pLmax_ may be compared to Figure 5 of Holzfuss' work.

#### Power-law liquid
Using [powerlaw.apess](powerlaw.apecss) with ````./build/ultrasound_apecss -options powerlaw.apecss -freq 636619 -amp 25331 -tend 25e-6````, this example reproduces Figure 2c of [Kaykanat & Uguz, _The European Physical Journal Special Topics_ 233 (2024), 1625](https://doi.org/10.1140/epjs/s11734-024-01174-7).

#### Kelvin-Voigt
Using [kelvinvoigt.apess](kelvinvoigt.apecss) with ````./build/ultrasound_apecss -options kelvinvoigt.apecss -tend 6e-6 -freq 1e6 -amp 3e6````, this example reproduces Figure 5b of [Yang & Church, _Journal of the Acoustical Society of America_ 118 (2005), 3595](https://doi.org/10.1121/1.2118307).

#### Zener
Using [zener.apess](zener.apecss) with ````./build/ultrasound_apecss -options zener.apecss -tend 5e-6 -freq 1e6 -amp 1e6````, this example reproduces Figure 5b of [Zilonova et al., _Ultrasonics Sonochemistry_ 40 (2018), 900](https://doi.org/10.1016/j.ultsonch.2017.08.017).

#### Oldroyd-B
Using [oldroydb.apess](oldroydb.apecss) with ````./build/ultrasound_apecss -options oldroydb.apecss -tend 3e-6 -freq 3e6 -amp 400e3````, this example reproduces Figure 1 (De = 1, lower solid line) of [Jimenez-Fernandez & Crespo, _Ultrasonics_ 43 (2005), 643](https://doi.org/10.1016/j.ultras.2005.03.010).
