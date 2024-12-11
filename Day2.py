{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM4jjWI2ZTwIHghhNb59jG5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MrTahir2005/TahirPython/blob/main/Day2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#                                      # **DAY 02** **"
      ],
      "metadata": {
        "id": "Prltrd2f7VLK"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **CONTROL FLOW AND LOOPS** **Conditional** **Statements**"
      ],
      "metadata": {
        "id": "Tuoz2E1S0Uuw"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**IF** **STATEMENT**"
      ],
      "metadata": {
        "id": "6ulYOtG212i5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "age=18\n",
        "if age>=18:\n",
        "  print(\"You are eligible to vote\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "seqC1b4417Iv",
        "outputId": "bae839e5-b637-435d-edcd-ca510897046c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You are eligible to vote\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **if-else Statements**"
      ],
      "metadata": {
        "id": "C1Tp0MVV2RKU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num=int(input(\"Enter a number: \"))\n",
        "if num%2==0:\n",
        "  print(\"The number is even\")\n",
        "else:\n",
        "  print(\"The number is odd\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "EkJuoRd12pLM",
        "outputId": "98425061-f8a6-419f-f403-a6286f2ea6ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 5\n",
            "The number is odd\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **IF-ELIF-ELSE STATEMENT**\n"
      ],
      "metadata": {
        "id": "T5diHsHT3Fgx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Marks=int(input('Enter your marks:'))\n",
        "if Marks>=90:\n",
        "  print('Grade:A')\n",
        "elif Marks>=75:\n",
        "  print('Grade B:')\n",
        "elif Marks>=50:\n",
        "  print('Grade C:')\n",
        "else:\n",
        "  print('Grade F:')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DbZatYNm3loS",
        "outputId": "04c93c6e-8895-4a49-b11c-7aa7579f7ac6",
        "collapsed": true
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your marks:55\n",
            "Grade C:\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Loops for 'LOOPS\n",
        "\n"
      ],
      "metadata": {
        "id": "OqhKRSUN5V1w"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5):\n",
        "  print(\"Iteration:\",i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "ecyO6J1u55-B",
        "outputId": "f337b2fa-592b-4499-a29f-195ba8e84d0b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Iteration: 0\n",
            "Iteration: 1\n",
            "Iteration: 2\n",
            "Iteration: 3\n",
            "Iteration: 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5,10):\n",
        "  print(\"Iteration:\",i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "42ncAqMp6Ul8",
        "outputId": "1f701f58-f6fb-43f5-97a6-a0aad09e9110"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Iteration: 5\n",
            "Iteration: 6\n",
            "Iteration: 7\n",
            "Iteration: 8\n",
            "Iteration: 9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range (5,50,10):\n",
        "  print(\"Iteration:\",i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "XY11aoKc6_8y",
        "outputId": "3c8323ad-9cd1-4f92-b339-c0b3fc6a9368"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Iteration: 5\n",
            "Iteration: 15\n",
            "Iteration: 25\n",
            "Iteration: 35\n",
            "Iteration: 45\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **WHILE LOOP**"
      ],
      "metadata": {
        "id": "uBy13Pp676OP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "count=0\n",
        "while count<5:\n",
        "  print(\"Count:\",count)\n",
        "  count+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "gcxUlxol8HhS",
        "outputId": "bac4537c-4400-4f95-969e-648acc31475d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Count: 0\n",
            "Count: 1\n",
            "Count: 2\n",
            "Count: 3\n",
            "Count: 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#                  **CONTROL FLOW TOOLS**\n",
        "\n"
      ],
      "metadata": {
        "id": "dL_DNvdJ8hMk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# break\n",
        "for i in range(10):\n",
        "  if i==5:\n",
        "    break\n",
        "  print(i)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "hpi-Q16F8_tt",
        "outputId": "10c5b190-21b4-4993-c1e4-aaa5273fc15d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# continue\n",
        "for i in range(10):\n",
        "  if i==5:\n",
        "    continue\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "R3Gm3aQG905v",
        "outputId": "07ebeb7a-4ae1-4ab2-c325-70c12d3dba50"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# pass\n",
        "for i in range(10):\n",
        "  if i==5:\n",
        "    pass\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "T_xP1Gwl-iqs",
        "outputId": "2877a5de-c40c-4a2a-ebd3-4deb8a9db6cc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "xNR_VXx_AeY1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# ***HANDS ON PRACTICE***"
      ],
      "metadata": {
        "id": "u6DwodipCL1K"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# odd or even\n",
        "X=int(input(\"ENTER A NUMBER:\"))\n",
        "if X%2==0:\n",
        "  print(\"EVEN NUMBER\")\n",
        "else:\n",
        "  print(\"Odd NUMBER\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "LB2aFCIKCPfg",
        "outputId": "43bcd079-b5d0-46c2-b358-c8a2fc0b2393"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ENTER A NUMBER:55\n",
            "Odd NUMBER\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# SUM OF NUMBERS IN A GIVEN RANGE\n",
        "start=int(input(\"Enter the start of the range:\"))\n",
        "end=int(input(\"Enter the end of the range:\"))\n",
        "sum=0\n",
        "for i in range(start,end+1):\n",
        "  sum+=i\n",
        "print(\"The sum of numbers from\",start,\"to\",end,\"is\",sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "tlmvwl5gC0o7",
        "outputId": "7312b93d-1e6a-4f04-caf9-068bbde5d271"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the start of the range:5\n",
            "Enter the end of the range:10\n",
            "The sum of numbers from 5 to 10 is 45\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Factorial\n",
        "num=int(input(\"Enter a number:\"))\n",
        "factorial=1\n",
        "for i in range (1,num+1):\n",
        "  factorial*=i\n",
        "print(\"The factorial is:\",factorial)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "s3ubKCQCFWjr",
        "outputId": "d4232dfb-8758-462d-de2c-2b5cd1251a2f"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number:12\n",
            "The factorial is: 479001600\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# FIBONACCI SEQUENCE\n",
        "n=int(input(\"Enter the number of terms:\"))\n",
        "a,b=0,1\n",
        "for _ in range(n):\n",
        "  print(a,end=\" \")\n",
        "  a,b=b,a+b"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "qkMt1v8GIHWy",
        "outputId": "60684f1f-cfe1-442a-bb7c-0b74abe2abac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of terms:5\n",
            "0 1 1 2 3 "
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **SIMPLE CALCULATOR USING IF-ELSE**"
      ],
      "metadata": {
        "id": "Ezh7M0uNUz7_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num1=float(input(\"Enter the first number:\"))\n",
        "num2=float(input(\"Enter the second number:\"))\n",
        "operation=input(\"Enter the operation(+,-,*,/,//,%,**):\")\n",
        "if operation=='+':\n",
        "  print(\"Result:\",num1 + num2)\n",
        "elif operation=='-':\n",
        "  print(\"Result:\",num1 - num2)\n",
        "elif operation=='*':\n",
        "  print(\"Result:\",num1 * num2)\n",
        "elif operation=='/':\n",
        "  print(\"Result:\",num1 / num2)\n",
        "elif operation=='//':\n",
        "  print(\"Result:\",num1 // num2)\n",
        "elif operation=='%':\n",
        "  print(\"Result:\",num1 % num2)\n",
        "elif operation=='**':\n",
        "  print(\"Result:\",num1 ** num2)\n",
        "else:\n",
        "  print(\"Invalid operation\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "NnpW2YaSUvv6",
        "outputId": "29f995cc-0f17-419b-f339-8d5676d736b4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first number:5\n",
            "Enter the second number:6\n",
            "Enter the operation(+,-,*,/,//,%,**):%\n",
            "Result: 5.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# CHECK LEAP YEAR\n",
        "year=int(input(\"Enter a year:\"))\n",
        "if(year%4==0 and year%100!=0) or (year%400==0):\n",
        "   print(year,\"is a leap year\")\n",
        "else:\n",
        "  print(year,\"is not a leap year\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "TnZIUk3MeJGN",
        "outputId": "e234087f-ce70-4a32-d758-0bbed731e23f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a year:2024\n",
            "2024 is a leap year\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# FIND THE LARGEST OF THREE NUMBERS\n",
        "num1=float(input(\"Enter the first number:\"))\n",
        "num2=float(input(\"Enter the second number:\"))\n",
        "num3=float(input(\"Enter the third number:\"))\n",
        "if num1>=num2 and num1>num3:\n",
        "  print(\"The largest number is:\",num1)\n",
        "elif num2>=num1 and num2>=num3:\n",
        "  print(\"The largest number is:\",num2)\n",
        "else:\n",
        "  print(\"The largest number is:\",num3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "qjzD1N6RgdkL",
        "outputId": "5d877c64-ca9e-4b9b-f675-0450a97e7a7f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first number:69\n",
            "Enter the second number:69\n",
            "Enter the third number:69\n",
            "The largest number is: 69.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# CHECK POSITIVE NEGATIVE OR ZERO\n",
        "a=int(input('Enter a Number:'))\n",
        "if a>0:\n",
        "  print('The number is positive')\n",
        "elif a<0:\n",
        "  print('The number is negative')\n",
        "else:\n",
        "   print('The number is zero')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "YjdcjQJUicws",
        "outputId": "6171aac6-acae-4b2f-c7f7-b0eb8a5a489b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a Number:-5\n",
            "The number is negative\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# SUM OF ALL EVEN NUMBERS\n",
        "start=int(input(\"Enter the start of the range:\"))\n",
        "end=int(input(\"Enter the end of the range:\"))\n",
        "sum_even=0\n",
        "for i in range(start,end+1):\n",
        "  if i%2==0:\n",
        "    sum_even+=i\n",
        "print(\"The sum of even numbers from\",start,\"to\",end,\"is\",sum_even)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6XIAGJUopNiz",
        "outputId": "a01bd780-598f-4be7-a422-f6166f78ca92",
        "collapsed": true
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the start of the range:5\n",
            "Enter the end of the range:10\n",
            "The sum of even numbers from 5 to 10 is 24\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **SIMPLE PYTHON QUESTIONS BASED ON CONTROL FLOW AND LOOP**\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "sKNCGrmxFuyw"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1.Write a program that checks if a character is a vowel or a consonant\n"
      ],
      "metadata": {
        "id": "Kt5Rur8mGhzr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "letter=input(\"Enter a letter:\")\n",
        "if letter in 'aeiou':\n",
        "  print(letter,  \"is a vowel\")\n",
        "else:\n",
        "  print(letter, \"is a consonant\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "_ht7S2xSGw4d",
        "outputId": "432c9cbf-d13c-4427-c59d-0b68701897ae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a letter:b\n",
            "b is a consonant\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.Write a program to determine if a given number is divisible by 5 and 3.\n",
        "\n"
      ],
      "metadata": {
        "id": "i1jva9HpJwlp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"Enter a number: \"))\n",
        "if num % 5 == 0 and num % 3 == 0:\n",
        "    print(num, \"is divisible by both 5 and 3\")\n",
        "else:\n",
        "    print(num, \"is not divisible by both 5 and 3\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "EJoGDbtmJvQs",
        "outputId": "f8d98a8d-65c9-4772-ad31-2b21281ad95a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 11\n",
            "11 is not divisible by both 5 and 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.Write a program to print numbers from 1 to 10."
      ],
      "metadata": {
        "id": "A9tbY6opK0PB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1, 11):\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "W8TQVfViK72i",
        "outputId": "3f118afc-8081-46af-f75e-68887bf6dc33"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4.Write a program to print the multiplication table of 5\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "m8Q5-HfTLNEL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "number=5\n",
        "for i in range(1, 11):\n",
        "      product = number * i\n",
        "      print(f\"{number} x {i} = {product}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "TeQvQyyiLO_n",
        "outputId": "2206d5c2-a570-4930-cb54-cf1bb5b7ac86"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 x 1 = 5\n",
            "5 x 2 = 10\n",
            "5 x 3 = 15\n",
            "5 x 4 = 20\n",
            "5 x 5 = 25\n",
            "5 x 6 = 30\n",
            "5 x 7 = 35\n",
            "5 x 8 = 40\n",
            "5 x 9 = 45\n",
            "5 x 10 = 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5.Write a program to calculate the sum of the first 10 natural numbers"
      ],
      "metadata": {
        "id": "vxRnKJIjLtrj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "total_sum = 0\n",
        "for i in range(1, 11):\n",
        "    total_sum += i\n",
        "print(\"The sum of the first 10 natural numbers is:\", total_sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LPMx9N3-MDu6",
        "outputId": "9ee2f6c8-ccaa-40fc-83ca-68ee3b84e888"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The sum of the first 10 natural numbers is: 55\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6.Write a program to print all even numbers between 1 and 20"
      ],
      "metadata": {
        "id": "8drWySRfMV6i"
      }
    },
    {
      "source": [
        "for i in range(1, 21):\n",
        "    if i % 2 == 0:\n",
        "        print(i)"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "rXA4V5xqMjkV",
        "outputId": "ed0a83f8-70e5-4327-c07e-3e40f8e6d2fd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7.Write a program to print all odd numbers between 1 and 20\n",
        "\n"
      ],
      "metadata": {
        "id": "ieWNGjOQM2mL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,21,2):\n",
        "  print(i)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "fwHCcHcTNLZD",
        "outputId": "d1352a76-6057-400a-da8c-1c61a8efc5a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "3\n",
            "5\n",
            "7\n",
            "9\n",
            "11\n",
            "13\n",
            "15\n",
            "17\n",
            "19\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8.Write a program that stops printing numbers from 1 to 10 when it encounters the number 5"
      ],
      "metadata": {
        "id": "_kLvDEBINlg1"
      }
    },
    {
      "source": [
        "for i in range(1, 11):\n",
        "     print(i)\n",
        "     if i == 5:\n",
        "       break"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "dCXKhXF7OWWT",
        "outputId": "e13d8c2b-e051-4f19-b030-815b7a3812e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "9.Write a program that skips printing the number 4 in a loop that goes from 1 to 5."
      ],
      "metadata": {
        "id": "jjHGQL8aOw6b"
      }
    },
    {
      "source": [
        "for i in range(1, 6):\n",
        "  if i == 4:\n",
        "    continue\n",
        "  print(i)"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "obHMelwbPESC",
        "outputId": "a8d1a763-b7d9-4871-a9ed-baf1128956c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "10.Write a program to iterate through a list of fruits and print each fruit's name."
      ],
      "metadata": {
        "id": "ZXtofWFCPevj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "fruits = [\"apple\", \"banana\", \"cherry\", \"date\", \"elderberry\"]\n",
        "for fruit in fruits:\n",
        "     print(fruit)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "nHrCADdbPhGr",
        "outputId": "07370746-436a-4ff0-f916-edd0affd3a5a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "apple\n",
            "banana\n",
            "cherry\n",
            "date\n",
            "elderberry\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "11.Write a program to calculate the sum of numbers until the user enters 0"
      ],
      "metadata": {
        "id": "_Ss5LcAWQcci"
      }
    },
    {
      "source": [
        "total_sum = 0\n",
        "while True:\n",
        "    number = int(input(\"Enter a number (enter 0 to stop): \"))\n",
        "    if number == 0:\n",
        "        break\n",
        "    total_sum += number\n",
        "\n",
        "print(\"The sum of the numbers is:\", total_sum)"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4UOO4RLnQqas",
        "outputId": "9ed2f3ef-2a55-4f03-c3db-242cb087fdce"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number (enter 0 to stop): 55\n",
            "Enter a number (enter 0 to stop): 66\n",
            "Enter a number (enter 0 to stop): 1\n",
            "Enter a number (enter 0 to stop): 2\n",
            "Enter a number (enter 0 to stop): 0\n",
            "The sum of the numbers is: 124\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "12.Write a program to reverse a given number using a while loop"
      ],
      "metadata": {
        "id": "CWCxb_JlRBnO"
      }
    },
    {
      "source": [
        "number = int(input(\"Enter a number: \"))\n",
        "reversed_number = 0\n",
        "while number > 0:\n",
        "    remainder = number % 10\n",
        "    reversed_number = (reversed_number * 10) + remainder\n",
        "    number //= 10\n",
        "print(\"Reversed Number:\", reversed_number)"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "-bSHRys0RJ7P",
        "outputId": "05a36017-bed5-418b-ae23-59eac3af50d2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 65\n",
            "Reversed Number: 56\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "13.Write a program to keep asking for a number until the user enters a negative number"
      ],
      "metadata": {
        "id": "icjRhUCxTeH9"
      }
    },
    {
      "source": [
        "while True:\n",
        "    number = int(input(\"Enter a number: \"))\n",
        "    if number < 0:\n",
        "        break\n",
        "    print(\"You entered:\", number)\n",
        "print(\"You entered a negative number. Exiting.\")"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "rrhPSA5zT13k",
        "outputId": "7b9cfd53-3cfa-4b95-db35-61095172746b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 55\n",
            "You entered: 55\n",
            "Enter a number: -9\n",
            "You entered a negative number. Exiting.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "14.Write a program to count down from 10 to 1."
      ],
      "metadata": {
        "id": "aW20Lw4QUFIy"
      }
    },
    {
      "source": [
        "for i in range(10, 0, -1):\n",
        "  print(i)"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "8xm4PLiSUSlR",
        "outputId": "5f2c3520-a503-4094-ecd9-d387b1942464"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "15.Write a program to print a 3x3 matrix of * symbols"
      ],
      "metadata": {
        "id": "3V7QPUIEUYz2"
      }
    },
    {
      "source": [
        "for i in range(3):\n",
        "    for j in range(3):\n",
        "        print(\"*\", end=\" \")\n",
        "    print()"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iEv_MyNxUr-7",
        "outputId": "5b58b82e-3c3f-4075-b974-6a2a774c9d1d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "* * * \n",
            "* * * \n",
            "* * * \n"
          ]
        }
      ]
    }
  ]
}