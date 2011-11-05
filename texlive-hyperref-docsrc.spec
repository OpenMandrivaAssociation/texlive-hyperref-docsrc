# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyperref-docsrc
Version:	20111103
Release:	1
Summary:	TeXLive hyperref-docsrc package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperref-docsrc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperref-docsrc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive hyperref-docsrc package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/hyperref-docsrc/README
%doc %{_texmfdistdir}/doc/latex/hyperref-docsrc/paperslides99.zip
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
