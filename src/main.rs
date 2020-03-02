#[macro_use]
extern crate clap;
use clap::App;


fn main() {
    let yaml = load_yaml!("cli.yaml");
    let matches = App::from_yaml(yaml).get_matches();

    let config = matches.value_of("config");
    let debug = matches.value_of("debug");
    

    if let Some(sub) = matches.subcommand_matches("get") {
        if let Some(file) = sub.value_of("INPUT") {
        println!("Using sub input file: {:?}", file);
        println!("Value for config: {:?}", config);
        }
    }
    else {
        if let Some(file) = matches.value_of("INPUT") {
        println!("Using input file: {:?}", file);
        }
    }

    println!("Hello, world!");
}
