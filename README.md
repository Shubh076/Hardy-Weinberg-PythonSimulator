# Hardy-Weinberg-PythonSimulator
Python implementation of the Hardy-Weinberg equilibrium to calculate and visualize genotype frequencies(AA, Aa, aa) from allele frequencies

## What is Hardy-Weinberg Equilibrium

The hardy-weinberg principle states that allele and genotype frequencies in a population will remain constant across generations in the absence of evolutionary influences such as mutation, migration, natural selection, random mating, and infinite population size

The equilibrium is described by the equation:

```
p^2 + 2pq + q^2 = 1
```

Where:
- `p` = frequency of the dominant allele (A)
- `q` = frequency of the recessive allele (a), where `p + q = 1`
- `p^2` = frequency of homozygous dominant genotype (AA)
- `2pq` = frequency of heterozygous genotype (Aa)
- `q^2` = frequency of homozygous recessive genotype (aa)

## Features 

- Calculates genotype frequencies (AA, Aa, aa) from given allele frequencies
- Verifies that frequencies sum to 1
- Generates a labeled bar graph of genotype distribution

## Requirements

All dependencies are listed in `requirements.txt`

```bash
pip install -r requirements.txt
```

## Usage 

```bash
python HW SIM.py 
```

## Customization 

Change the value of `p` to model different allele frequencies and see how the genotype distribution shifts. `q` is automatically calculated as `1 - p`.

## Example 

Running the default parameters (`p=0.6`, `q=0.4`) produces:

![image alt](https://github.com/Shubh076/Hardy-Weinberg-PythonSimulator/blob/6588bbd8a3aca140542a07316cff38d4f86a8fe1/HW_sim.png)

## License 
This project is licensed under MIT license
