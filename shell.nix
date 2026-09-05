let
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-unstable") {};
in

pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      requests
    ]))
  ];
}
