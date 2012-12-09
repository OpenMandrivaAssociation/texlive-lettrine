# revision 27185
# category Package
# catalog-ctan /macros/latex/contrib/lettrine
# catalog-date 2012-07-20 19:39:58 +0200
# catalog-license lppl
# catalog-version 1.63
Name:		texlive-lettrine
Version:	1.63
Release:	1
Summary:	Typeset dropped capitals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lettrine
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lettrine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lettrine.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lettrine.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The lettrine package supports various dropped capitals styles,
typically those described in the French typographic books. In
particular, it has facilities for the paragraph text's left
edge to follow the outline of capitals that have a regular
shape (such as "A" and "V").

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lettrine/lettrine.cfg
%{_texmfdistdir}/tex/latex/lettrine/lettrine.sty
%{_texmfdistdir}/tex/latex/lettrine/optfile.cfl
%{_texmfdistdir}/tex/latex/lettrine/pacl.cfl
%{_texmfdistdir}/tex/latex/lettrine/padl.cfl
%{_texmfdistdir}/tex/latex/lettrine/pzc2.cfl
%{_texmfdistdir}/tex/latex/lettrine/pzc3.cfl
%doc %{_texmfdistdir}/doc/latex/lettrine/README
%doc %{_texmfdistdir}/doc/latex/lettrine/W.eps
%doc %{_texmfdistdir}/doc/latex/lettrine/W.pdf
%doc %{_texmfdistdir}/doc/latex/lettrine/demo-de.pdf
%doc %{_texmfdistdir}/doc/latex/lettrine/demo-de.tex
%doc %{_texmfdistdir}/doc/latex/lettrine/demo.pdf
%doc %{_texmfdistdir}/doc/latex/lettrine/demo.tex
%doc %{_texmfdistdir}/doc/latex/lettrine/lettrine.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lettrine/lettrine.dtx
%doc %{_texmfdistdir}/source/latex/lettrine/lettrine.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.63-1
+ Revision: 812565
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 753275
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 718846
- texlive-lettrine
- texlive-lettrine
- texlive-lettrine
- texlive-lettrine

