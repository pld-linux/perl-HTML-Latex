#
# Conditional build:
# _with_tests - perform "make test" (failed on my machine)
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Latex
Summary:	HTML::Latex - Creates a Latex file from an HTML file
Summary(pl):	Modu³ HTML::Latex - tworz±cy plik LaTeX z pliku HTML
Name:		perl-%{pdir}-%{pnam}
Version:	1.0
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%{?_with_tests:BuildRequires:	perl-HTML-Tree }
%{?_with_tests:BuildRequires:	perl-XML-Simple >= 1.04}
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts properly formatted HTML files, filehandles, or strings to
LaTeX. It offers several options in processing, such a the ignoring of
tags, the configuration of the TeX, and downloading of URLs. It is
also much easier to extend than any other html2latex converter.

%description -l pl
Modu³ ten konwertuje odpowiednio sformatowane pliki HTML, uchwyty
plików lub ³añcuchy znaków do LaTeXa. Oferuje przy przetwarzaniu kilka
opcji, takich jak ignorowanie znaczników, konfiguracja TeXa oraz
¶ci±ganie odno¶ników. Jest du¿o prostszy do rozbudowywania ni¿
jakikolwiek inny konwerter html2latex.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README TODO
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
