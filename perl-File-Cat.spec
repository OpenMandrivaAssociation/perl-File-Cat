%define	module	File-Cat
%define	name	perl-%{module}
%define	version	1.2
%define	release	%mkrel 4

Name:		%{name}
Version:	%perl_convert_version 1.2
Release:	1
Summary:	Perl implementation of cat(1)
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/F/FI/FIMM/File-Cat-1.2.tar.gz
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




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2-4mdv2010.0
+ Revision: 430443
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.2-3mdv2009.0
+ Revision: 256871
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.2-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Mar 04 2007 Olivier Blin <oblin@mandriva.com> 1.2-1mdv2007.0
+ Revision: 132670
- initial Mandriva release
- Create perl-File-Cat


