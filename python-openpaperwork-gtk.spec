%global module openpaperwork-gtk

Summary:	OpenPaperwork GTK plugins
Name:		python-%{module}
Version:	2.2.0
Release:	1
License:	GPL-3.0-or-later
Group:		Development/Python
URL:		https://pypi.org/project/openpaperwork-gtk/
Source0:	https://pypi.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz
Patch0:		python-openpaperwork-gtk-2.2.0-fix_version_path.patch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pygobject)

Requires:       python%{pyver}dist(pygobject)
Requires:       gdk-pixbuf2.0
Requires:       gtk+3.0
Requires:       %{_lib}handy1_0
Requires:       %{_lib}notify4
Requires:       pango

BuildArch:	noarch

%description
OpenPaperwork GTK plugins.

%files
%{py_puresitedir}/openpaperwork_gtk
%{py_puresitedir}/openpaperwork_gtk-*.*-info

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

