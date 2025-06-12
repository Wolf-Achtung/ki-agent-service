def merge_sections(executive, strategy, roadmap, resources):
    return "\n\n".join([
        "## Executive Summary\n" + executive,
        "## Strategische Analyse\n" + strategy,
        "## Empfehlungen & Roadmap\n" + roadmap,
        "## Ressourcen & Tipps\n" + resources
    ])
