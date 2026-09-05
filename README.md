# Proton for No Raids

Parte pública do Proton for No Raids, meu projeto de proteção e moderação para servidores do Discord.

O sistema completo não fica neste repositório porque algumas regras de detecção, credenciais e partes de segurança precisam continuar privadas.

## Incluído

- helpers de embeds;
- cache simples de configurações por servidor;
- verificações de permissão e hierarquia;
- modelos de eventos de segurança;
- exemplo de integração;
- testes.

## Não incluído

- regras e limites do anti-raid;
- detecção de anúncios e vendas;
- OCR e análise de imagens;
- prompts e configuração de moderação por IA;
- whitelist e bypasses;
- ações automáticas de punição;
- banco e credenciais de produção;
- painéis internos.

## Estrutura

```text
src/proton_no_raids_public/
  embeds.py
  permissions.py
  security_events.py
  settings_cache.py
examples/
tests/
docs/
```

## Rodando

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## Segurança

Nunca coloque `.env`, token de bot, service-role do Supabase ou outras credenciais reais neste repositório. Veja [`SECURITY.md`](SECURITY.md) para mais detalhes.
