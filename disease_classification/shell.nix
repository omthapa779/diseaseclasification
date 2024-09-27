{ pkgs ? import <nixpkgs> {} }: 
let 
  python = pkgs.python311;  # or python310 if you prefer
in 
pkgs.mkShell {
  buildInputs = [
    python
    (python.withPackages (ps: with ps; [ django ]))
  ];
}
