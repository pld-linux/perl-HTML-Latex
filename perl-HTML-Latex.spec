#
# Conditional build:
%bcond_with	tests	# perform "make test" (failed on my machine)

%define		pdir	HTML
%define		pnam	Latex
Summary:	HTML::Latex Perl module - creates a LaTeX file from an HTML file
Summary(pl.UTF-8):	Moduł Perla HTML::Latex - tworzenie pliku w LaTeXu z pliku HTML
Name:		perl-HTML-Latex
Version:	1.0
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b15c98fe9105340060e55e11c17747cb
URL:		http://search.cpan.org/dist/HTML-Latex/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-XML-Simple >= 1.04
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts properly formatted HTML files, filehandles, or strings to
LaTeX. It offers several options in processing, such a the ignoring of
tags, the configuration of the TeX, and downloading of URLs. It is
also much easier to extend than any other html2latex converter.

%description -l pl.UTF-8
Moduł ten konwertuje odpowiednio sformatowane pliki HTML, uchwyty
plików lub łańcuchy znaków do LaTeXa. Oferuje przy przetwarzaniu kilka
opcji, takich jak ignorowanie znaczników, konfiguracja TeXa oraz
ściąganie odnośników. Jest dużo prostszy do rozbudowywania niż
jakikolwiek inny konwerter html2latex.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README TODO
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
