
### Frost calculation in South America from GOES land surface temperature (LST) data

#### Description:
This GitHub repository is dedicated to the automation of frost calculation in South America. To do so, the code performs gap filling in GOES land surface temperature (LST) data, specifically focusing on cases of invalid or cloudy data. The methodology employed leverages Weather Forecast System (WFS) model data to improve the accuracy and integrity of the GOES LST dataset.

#### Features:

1. **Automated Gap-Filling:**
   - The repository provides automated tools for identifying and filling gaps in the GOES LST data.
   - Utilizes the WFS model data as a supplementary source to enhance the temporal and spatial coverage.

2. **Cloudy Data Handling:**
   - Specialized algorithms address the challenges posed by cloudy data, ensuring a more comprehensive and reliable LST dataset.

3. **Integration with GOES Data:**
   - Seamless integration with GOES satellite data, maintaining the original structure while improving data quality.

#### Requirements:
- Python 3.x
- Dependencies listed in environment.yml

#### Installation:

```bash
conda create -n env_frosts -f environment.yml
```

#### Contributors:
- [German Taveira]
- [Francisco Corvalán]
- [David Elías]
- [Axel Elseser]
- [Malvina Serra]
- [Sol Villella]
- [Mariana Correa]
- [Gisselle Bertola]
- [Agustina González]
- [Emmanuel Leizica]
- [Kevin Yaringaño]
- [Mirian Villalobos]
- [Andrés Rosero]


#### License:
This project is licensed under [License Name] - see the [LICENSE](LICENSE) file for details.

#### Acknowledgments:
- The project acknowledges the contributions of the WFS model developers.
- Appreciation to the creators and maintainers of the GOES dataset.

Feel free to contribute to the project and open issues for any suggestions or improvements. Your collaboration is highly valued.
