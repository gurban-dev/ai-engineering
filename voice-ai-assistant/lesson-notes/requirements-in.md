# Managing Python Dependencies

The `requirements.in` file lists the external Python packages your project needs. It serves as the input for `pip-compile`, which resolves dependencies and generates a `requirements.txt` file with pinned package versions.

## 1. Add dependencies

List your project's external dependencies in `requirements.in`.

For example:

```text
numpy==2.5.4

--extra-index-url https://download.pytorch.org/whl/cpu

torch==2.15.0
pip-tools
```

You generally do not need to list packages included in Python's standard library.

## 2. Generate `requirements.txt`

Run:

```bash
pip-compile requirements.in
```

`pip-compile` resolves the dependencies and generates `requirements.txt` with pinned versions.

The generated file reflects the packages in `requirements.in` and their dependencies. Packages that are neither listed in `requirements.in` nor required by its dependencies will be removed from requirements.txt after running pip-compile requirements.in.

**Important:** Edit `requirements.in`, not `requirements.txt`, because the latter is generated automatically.

## 3. Synchronize the virtual environment

Run:

```bash
pip-sync requirements.txt
```

`pip-sync` installs the packages listed in `requirements.txt` and uninstalls packages that are not listed.

**Note:** Run these commands inside your project's activated virtual environment. Make sure `requirements.txt` includes everything your project needs, as `pip-sync` can uninstall other packages.

## 4. Typical workflow

Whenever you add or remove a dependency:

1. Update `requirements.in`.
2. Run `pip-compile requirements.in` to regenerate `requirements.txt`.
3. Run `pip-sync requirements.txt` to synchronize your environment.