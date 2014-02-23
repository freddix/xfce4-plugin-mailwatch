%define		org_name	xfce4-mailwatch-plugin

Summary:	Mailwatch plugin for XFCE panel
Name:		xfce4-plugin-mailwatch
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mailwatch-plugin/1.2/%{org_name}-%{version}.tar.bz2
# Source0-md5:	7263114ec0f2987a3aff15afeeb45577
URL:		http://goodies.xfce.org/projects/panel-plugins/template
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfce4-panel-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Template plugin for XFCE panel.

%prep
%setup -qn %{org_name}-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libmailwatch.so
%{_datadir}/xfce4/panel/plugins/mailwatch.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

