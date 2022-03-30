cat << EOF
Running Video-Convertor v1.4
EOF

export PS1="\[\e[36m\]\${OKTETO_NAMESPACE:-okteto}:\[\e[32m\]\${OKTETO_NAME:-dev} \[\e[m\]\W> "
