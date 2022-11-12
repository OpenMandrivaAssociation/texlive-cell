Name:		texlive-cell
Version:	42428
Release:	1
Summary:	Bibliography style for Cell
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cell
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cell.r42428.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cell.doc.r42428.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an "apa-like" style (cf. apalike.bst in the BibTeX
distribution), developed from the same author's JMB style. A
supporting LaTeX package is also provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/cell/cell.bst
%{_texmfdistdir}/tex/latex/cell/cell.sty
%doc %{_texmfdistdir}/doc/latex/cell/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
