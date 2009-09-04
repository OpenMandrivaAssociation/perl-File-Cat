%define	module	File-Cat
%define	name	perl-%{module}
%define	version	1.2
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl implementation of cat(1)
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/F/FI/FIMM/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}
Buildrequires:	perl-devel
Requires:	perl 
Buildarch:	noarch

%description
File::Cat is a module of adventure, danger, and low cunning. With it,
you will explore some of the most inane programs ever seen by
mortals. No computer should be without one!

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{perl_vendorlib}/File/Cat.pm
%{_mandir}/*/*


