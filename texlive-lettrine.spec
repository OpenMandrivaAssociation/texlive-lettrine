Name:		texlive-lettrine
Version:	2.22
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
%{_texmfdistdir}/tex/latex/lettrine
%doc %{_texmfdistdir}/doc/latex/lettrine
#- source
%doc %{_texmfdistdir}/source/latex/lettrine

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
