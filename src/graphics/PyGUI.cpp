//
// Created by per on 06.06.18.
//

#include "PyGUI.h"

#include <pybind11/embed.h> // everything needed for embedding
#include "../Game.h"


PyGUI::PyGUI(Game& game): game(game) {
    pybind11::initialize_interpreter();

    this->init_dependencies();
    this->init_argv();
    //this->init_cython();
    this->init_gui();
}


PyGUI::~PyGUI() {
    //pybind11::finalize_interpreter();
    std::cout << "what" << std::endl;
}

void PyGUI::init_dependencies(){
    pybind11::module subprocess = pybind11::module::import("subprocess");
    pybind11::module sys = pybind11::module::import("sys");
    auto args = pybind11::list();
    args.append(sys.attr("executable"));
    args.append("-m");
    args.append("pip");
    args.append("install");
    args.append("-r");
    args.append("../requirements.txt");
    args.append("--user");
    subprocess.attr("check_call")(args);
}

void PyGUI::init_argv(){
    pybind11::module sys = pybind11::module::import("sys");
    auto args = pybind11::list();
    args.append("");
    sys.attr("argv") = args;
}

void PyGUI::init_cython(){
    pybind11::module pyximport = pybind11::module::import("pyximport");
    pyximport.attr("install")();
}

void PyGUI::init_gui(){

    pybind11::module DeepRTS = pybind11::module::import("DeepRTS");
    pybind11::module::import("pygame");
    auto DeepRTS_Python = DeepRTS.attr("python");
    auto GUI = DeepRTS_Python.attr("GUI");
    auto GameBridge = DeepRTS_Python.attr("GameBridge");
    auto Config = DeepRTS_Python.attr("Config");

    gui = GUI(GameBridge(&game), 32, Config(true, true, true, false, true, false, true, false, 50));

}

