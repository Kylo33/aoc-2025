defmodule Solver do  
  def part1(input) do
    input
    |> String.split(~r"[-,]")
    |> Enum.map(&String.to_integer/1)
    |> Enum.chunk_every(2)
    |> Enum.flat_map(fn [first, last] ->
      first..last
      |> Enum.filter(fn val ->
        val
        |> Integer.to_string()
        |> String.match?(~r"^(\d+)\1$")
      end)
    end)
    |> Enum.sum()
  end

  def part2(input) do
    input
    |> String.split(~r"[-,]")
    |> Enum.map(&String.to_integer/1)
    |> Enum.chunk_every(2)
    |> Enum.flat_map(fn [first, last] ->
      first..last
      |> Enum.filter(fn val ->
        val
        |> Integer.to_string()
        |> String.match?(~r"^(\d+)\1+$")
      end)
    end)
    |> Enum.sum()
  end
end

input
|> Kino.Input.read()
|> Solver.part1()
|> IO.puts()

input
|> Kino.Input.read()
|> Solver.part2()
|> IO.puts()
