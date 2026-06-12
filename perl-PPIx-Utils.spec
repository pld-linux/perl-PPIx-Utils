#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	PPIx
%define		pnam	Utils
Summary:	PPIx::Utils - utility functions for PPI
Summary(pl.UTF-8):	PPIx::Utils - funkcje narzędziowe dla PPI
Name:		perl-PPIx-Utils
Version:	0.004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	24c275dd1b8b03bd4d21bf849f733b6a
URL:		https://metacpan.org/dist/PPIx-Utils
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-B-Keywords
BuildRequires:	perl-PPI
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PPIx::Utils is a collection of utility functions for working with PPI
documents, originally split out from Perl::Critic. The functions are
organised into submodules by the kind of task they perform
(classification, traversal, language).

%description -l pl.UTF-8
PPIx::Utils to zbiór funkcji narzędziowych do pracy z dokumentami PPI,
pierwotnie wydzielonych z modułu Perl::Critic. Funkcje są podzielone
na podmoduły według rodzaju zadania (klasyfikacja, przechodzenie po
drzewie, język).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README LICENSE
%{perl_vendorlib}/PPIx/Utils.pm
%{perl_vendorlib}/PPIx/Utils
%{_mandir}/man3/PPIx::Utils*.3pm*
