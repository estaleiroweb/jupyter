checar_instalar_pacote <- function(pacote) {
  if (!require(pacote, character.only = TRUE)) {
	print(pacote)
    # install.packages(pacote, dependencies = TRUE)
    # library(pacote, character.only = TRUE) # nolint
  }
}

# Pacotes necessarios - instalação
pacotes <- c(
  "evaluate",
  "IRkernel",
#   "conflicted",
#   "languageserver",
#   "curl",
#   "systemfonts",
#   "textshaping",
#   "httr",
#   "readxl",
#   "ragg",
#   "tidyverse", # manipulação de dados
#   "ggplot2", # visualização
#   "cowplot", # visualização - unir gráficos
#   "caret", # modelos estatísticos
#   "corrplot", # matriz de correlação

  # "nloptr",
  # "vegan",
  # "seriation",
  # "pmml",
  # "xgboost",
  # "lme4",
  # "jomo",
  # "mitml",
  # "arulesViz",
  # "mice",
  # "RODBC",

#   "rattle"
)

for (pacote in pacotes) {
  checar_instalar_pacote(pacote)
}
# install.packages("remotes")
# remotes::install_version("vegan", version = "2.5-6")
# library(tidyverse)
