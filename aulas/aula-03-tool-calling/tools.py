"""Ferramentas customizadas para o agente: calculadora e conversor de temperatura.

Demonstra como criar tools usando o decorator @tool do Agno.
As docstrings são usadas pelo LLM para entender quando usar cada ferramenta.
"""

from agno.tools import tool


@tool
def calculate(expression: str) -> str:
    """Avalia uma expressão matemática e retorna o resultado.

    Args:
        expression: Expressão matemática a ser avaliada. Exemplo: '2 + 3 * 4'

    Returns:
        O resultado do cálculo ou uma mensagem de erro.
    """
    # Funções permitidas para segurança (evita execução de código arbitrário)
    allowed_names = {
        "abs": abs,
        "round": round,
        "min": min,
        "max": max,
        "pow": pow,
        "int": int,
        "float": float,
    }
    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"Resultado de '{expression}' = {result}"
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    except Exception as e:
        return f"Erro ao avaliar '{expression}': {e}"


@tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> str:
    """Converte temperatura entre Celsius (C), Fahrenheit (F) e Kelvin (K).

    Args:
        value: Valor da temperatura a ser convertido.
        from_unit: Unidade de origem — 'C', 'F' ou 'K'.
        to_unit: Unidade de destino — 'C', 'F' ou 'K'.

    Returns:
        A temperatura convertida em formato legível.
    """
    from_unit = from_unit.upper().strip()
    to_unit = to_unit.upper().strip()

    valid_units = {"C", "F", "K"}
    if from_unit not in valid_units or to_unit not in valid_units:
        return (
            f"Erro: unidades devem ser {valid_units}. Recebido: de='{from_unit}', para='{to_unit}'."
        )

    if from_unit == to_unit:
        return f"{value}°{to_unit} (mesma unidade, conversão desnecessária)"

    # Converte para Celsius primeiro (passo intermediário)
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:  # K
        celsius = value - 273.15

    # Converte de Celsius para a unidade destino
    if to_unit == "C":
        result = celsius
    elif to_unit == "F":
        result = celsius * 9 / 5 + 32
    else:  # K
        result = celsius + 273.15

    return f"{value}°{from_unit} = {result:.2f}°{to_unit}"
