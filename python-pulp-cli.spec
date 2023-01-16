Name:           python-pulp-cli
Version:        0.16.0
Release:        1%{?dist}
Summary:        Command line interface to talk to pulpcore's REST API.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPLv2+
URL:            https://github.com/pulp/pulp-cli
Source:         %{pypi_source pulp-cli}

Patch:          deps.patch

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pulp-cli' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pulp-cli
Summary:        %{summary}

%description -n python3-pulp-cli %_description


%prep
%autosetup -p1 -n pulp-cli-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
# %%pyproject_check_import -t


%files -n python3-pulp-cli -f %{pyproject_files}


%changelog
* Fri Jan 13 2023 Pavel Raiskup <praiskup@redhat.com> - 0.16.0-1
- Initial package
