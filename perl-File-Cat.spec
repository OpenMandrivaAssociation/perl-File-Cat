%define	module	File-Cat
Name:		perl-%{module}
Version:	1.2
Release:	9
Summary:	Perl implementation of cat(1)
License:	GPL or Artistic
Group:		Development/Perl
Source:		https://cpan.metacpan.org/authors/id/F/FI/FIMM/File-Cat-%{version}.tar.gz
Url:		https://metacpan.org/dist/File-Cat
BuildRequires:	make
BuildRequires:	perl-devel
Requires:	perl 
BuildArch:	noarch

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
%makeinstall_std

%files 
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


