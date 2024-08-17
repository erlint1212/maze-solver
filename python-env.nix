# shell.nix

# If you are not using nixos, ignore this file
# TODO: Make this into a flake to make it reproducible, offender: pkgs = import <nixpkgs> {};

let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.tkinter
    ]))
  ];
  shellHook = ''
    export PS1="\n\[\033[1;32m\][python3_mazeSolver:\w]\$\[\033[0m\]"
  '';
}
