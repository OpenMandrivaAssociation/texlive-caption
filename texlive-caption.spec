# revision 24525
# category Package
# catalog-ctan /macros/latex/contrib/caption
# catalog-date 2011-11-06 19:24:15 +0100
# catalog-license lppl
# catalog-version 3.2d
Name:		texlive-caption
Version:	3.2d
Release:	1
Summary:	Customising captions in floating environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/caption
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The caption package provides many ways to customise the
captions in floating environments like figure and table, and
cooperates with many other packages. Facilities include
rotating captions, sideways captions, continued captions (for
tables or figures that come in several parts). A list of
compatibility notes, for other packages, is provided in the
documentation. The package also provides the "caption outside
float" facility, in the same way that simpler packages like
capt-of do. The package supersedes caption2.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/caption/bicaption.sty
%{_texmfdistdir}/tex/latex/caption/caption.sty
%{_texmfdistdir}/tex/latex/caption/caption2.sty
%{_texmfdistdir}/tex/latex/caption/caption3.sty
%{_texmfdistdir}/tex/latex/caption/ltcaption.sty
%{_texmfdistdir}/tex/latex/caption/newfloat.sty
%{_texmfdistdir}/tex/latex/caption/subcaption.sty
%doc %{_texmfdistdir}/doc/latex/caption/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/caption/README
%doc %{_texmfdistdir}/doc/latex/caption/bicaption.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption-deu.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption-eng.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption-rus.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption2.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption3.pdf
%doc %{_texmfdistdir}/doc/latex/caption/ltcaption.pdf
%doc %{_texmfdistdir}/doc/latex/caption/newfloat.pdf
%doc %{_texmfdistdir}/doc/latex/caption/subcaption.pdf
#- source
%doc %{_texmfdistdir}/source/latex/caption/bicaption.dtx
%doc %{_texmfdistdir}/source/latex/caption/caption-deu.tex
%doc %{_texmfdistdir}/source/latex/caption/caption-eng.tex
%doc %{_texmfdistdir}/source/latex/caption/caption-rus.tex
%doc %{_texmfdistdir}/source/latex/caption/caption.dtx
%doc %{_texmfdistdir}/source/latex/caption/caption.ins
%doc %{_texmfdistdir}/source/latex/caption/caption2.dtx
%doc %{_texmfdistdir}/source/latex/caption/caption3.dtx
%doc %{_texmfdistdir}/source/latex/caption/cat.eps
%doc %{_texmfdistdir}/source/latex/caption/elephant.eps
%doc %{_texmfdistdir}/source/latex/caption/ltcaption.dtx
%doc %{_texmfdistdir}/source/latex/caption/newfloat.dtx
%doc %{_texmfdistdir}/source/latex/caption/subcaption.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
