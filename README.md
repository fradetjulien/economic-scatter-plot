# economic-scatter-plot
Read from two files containing country names, their GDP and currency values. Combine the two files and randomly plot 10 countries in a scatter plot with one axis being currency value and the other being GDP.

## Installation

Python 3 and Pipenv are required in order to run this program.

### OSX

```bash
brew install python3
```
```bash
brew install pipenv
```

## Usage

If you want to test the script manually, you can achieve this by doing :

```bash
cd module
pipenv install
pipenv run python3 index.py
```

## Example

<img align="center" src="assets/cli-example.png" width="650">
<img align="center" src="assets/usage-example.png" width="850">

## Executable

If you want to build a cross-platform executable, you need to execute the following bash commands :

```bash
cd module
pipenv install
pipenv run pyinstaller index.py --onefile
```

The executable file will be located on the generated dist folder.

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
