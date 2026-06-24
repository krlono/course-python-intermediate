# Configuration Files

This folder contains a ready-to-use setup and examples of how to use configuration files in Python.

Configuration files are text files used to store settings and values that your program needs, such as file paths, time periods, and model parameters.  
It is a good practice to collect such variables in one place, in a configuration file, instead of having them scattered throughout the code.  
This way, you only need to update one location, and the code itself does not need to be changed.

A common type of configuration file is **[TOML](https://toml.io/en/)** (Tom's Obvious, Minimal Language).  
TOML is a file format that is easy to read and write, and it is popular among developers for configuration purposes.  
TOML files are typically organized into sections, each containing key-value pairs.  
See the examples below.

***

## Using Dynaconf to Read Configuration Files

We recommend using the **[Dynaconf](https://www.dynaconf.com/)** library to read and work with configuration files in Python.  
It supports, among other things, reuse of variables.

This means that you can reuse variables inside other variables in the configuration file.  
For example, you can define a year once and reuse it in a file name.

Dynaconf also supports validation, environments, and more.

Dynaconf uses two files placed in a `config` folder:

```text
├── config
    ├── settings.toml  # The configuration file itself
    └── config.py      # Loads the config file and exposes variables via a settings object
```

***

## Example Usage

### `settings.toml`

```toml
year = 2024
product_root_dir = "/buckets/product/metstat"
```

### Use in your code

```python
from config.config import settings

print(f"Year = {settings.year}")
print(f"Product root dir = {settings.product_root_dir}")
```

***

## Reusing Variables

Variable reuse is done using the `@format` syntax:

```toml
dapla_team = "tip-tutorials"
short_name = "metstat"  # short name of the statistic
product_root_dir = "@format gs://ssb-{this.dapla_team}-data-produkt-prod/{this.short_name}"
```

Here, `settings.product_root_dir` becomes:

```
gs://ssb-tip-tutorials-data-produkt-prod/metstat
```

***

## Using Environments

Environments can be used to define different configurations for, for example, production and testing, without redefining all variables.  
You only need to override what differs.

In this example, environments are used to switch between bucket paths in the form:

* `/buckets/product`
* `gs://ssb-tip-tutorials-data-produkt-prod/`

Environments are defined as sections in the `settings.toml` file, such as `[default]` and `[gsbuckets]`:

```toml
[default]
dapla_team = "tip-tutorials"
short_name = "metstat"  # short name of the statistic
kildedata_root_dir = "@format /buckets/kilde/{this.short_name}"
product_root_dir = "@format /buckets/product/{this.short_name}"
input_dir = "@format {this.product_root_dir}/input"
prepared_dir = "@format {this.product_root_dir}/prepared-data"
statistics_dir = "@format {this.product_root_dir}/statistics"
output_dir = "@format {this.product_root_dir}/output"

[gsbuckets]
kildedata_root_dir = "@format gs://ssb-{this.dapla_team}-data-kilde-prod/{this.short_name}"
product_root_dir = "@format gs://ssb-{this.dapla_team}-data-produkt-prod/{this.short_name}"
```

Note that you only need to define `kildedata_root_dir` and `product_root_dir` under the `[gsbuckets]` section.  
The other variables are automatically expanded based on the overridden root paths.

***

## Selecting Environment

You choose which environment to use in `config.py`, as shown here:

```python
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["settings.toml"],
    envvar_prefix="DYNACONF",
    environments=True,
    env="default",  # Change to "gsbuckets" to use Google Storage buckets
)
```
