#include <iostream>

#include "httplib.h"

int main() {
  using namespace httplib;

  Server svr;

  svr.Get("/hi", [](const Request &req, Response &res) {
    res.set_content("Hello World!", "text/plain");
  });

  svr.Get(R"(/numbers/(\d+))", [&](const Request &req, Response &res) {
    auto numbers = req.matches[1];
    res.set_content(numbers, "text/plain");
  });

  svr.Get("/stop", [&](const Request &req, Response &res) { svr.stop(); });

  std::cout << "Started." << std::endl;
  svr.listen("localhost", 1234);
}
