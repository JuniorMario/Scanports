package main

import ("fmt"; "net";"strings";"flag";"strconv")
func try_connect (ip string, port string){
  casado := ip + ":" + port
  c, err := net.Dial("tcp", casado)
  if err != nil {
    defer func() {
      str := recover()
      fmt.Println(str)
  }()
  panic("port " + port +  " closed")
  } else {
    fmt.Println("port " + port + " opened")
  }
  defer c.Close()
}
func get_args (input string) []string {
  var param []string
  if strings.Contains(input, "-"){
    par := strings.Split(input, "-")
    pi, err := strconv.Atoi(par[0])
    if err != nil {
      panic(err)
    }
    pf, err := strconv.Atoi(par[1])
    if err != nil {
      panic(err)
    }
    for i := pi; i <= pf; i++ {
      joãozin := strconv.Itoa(i)
      param = append(param, joãozin)
    }
  } else if strings.Contains(input, ",") {
    param = strings.Split(input, ",")
  } else {
    param = append(param, input)
  }
  return param
}
func main (){
  var ip = flag.String("ip", "127.0.0.1", "IP a ser scaneado.")
  var input = flag.String("port", "80", "Portas a serem scaneadas")
  flag.Parse()
  res := get_args(*input)
  for _, port := range res {
    try_connect(*ip, port)
  }
}
