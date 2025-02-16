## Inspiration
We’ve always been fascinated by how words connect us across time and cultures. Tracing the origins of a single word can reveal hidden stories and linguistic influences from centuries ago. We wanted to create a tool that merges **data visualization** and **AI-powered etymology** to bring those hidden stories to life in a fun, interactive way.

## What It Does
**Indo-European Language Family Tree & Etymology Explorer** is an interactive web application that lets you:
1. **Visualize** the Indo-European language family in a dynamic tree.
2. **Pan and zoom** around the tree to discover different language branches.
3. **Search** for a specific word’s etymology using an AI (OpenAI) backend, which returns detailed linguistic roots.
4. **Highlight** or explore how the queried word might connect to the tree’s branches.

## How We Built It
1. **Backend (Python + Flask)**: Handles requests to `/get_etymology`, uses OpenAI’s GPT-4 to generate etymological explanations.
2. **Frontend (HTML/CSS/JavaScript)**: 
   - **vis.js** renders the hierarchical tree with pan/zoom functionality.
   - A **background image** is drawn on the same canvas to give it a “tree trunk and leaves” aesthetic.
   - **Search** interface calls the Flask endpoint, displays results, and optionally highlights relevant nodes.
3. **Data Flattening**: We used a small hierarchical JSON of Indo-European branches, which we converted into nodes/edges for vis.js.

## Challenges We Ran Into
- **Aligning the tree**: Positioning the large background image so it matches the branching structure took trial and error with canvas transforms.
- **Merging AI calls**: Ensuring the backend route `/get_etymology` returned consistent data and handling errors from OpenAI.
- **Performance & layout**: Balancing node spacing, hierarchical layout, and large fonts so the tree remained readable.

## Accomplishments We’re Proud Of
- Successfully **integrated** an AI-based etymology lookup with a real-time **interactive tree** visualization.
- Created a **visually appealing** interface that encourages exploration and learning about linguistic roots.
- Overcame **coordinate system** headaches to make the background “move” in sync with the language nodes.

## What We Learned
- How to **draw images** on a vis.js canvas and apply the same transforms (scale, translate) as the node layout.
- The **importance of backend endpoints** (Flask) and structured JSON responses for a smooth frontend experience.
- Fine-tuning prompts for OpenAI to get **concise yet informative** linguistic explanations.

## What’s Next
- **Expand** the data: Include more branches, extinct languages, or additional language families.
- **Deeper AI** integration: Provide phonological evolution or morphological analysis with more advanced prompts.
- **User contributions**: Let people add words or personal notes to the tree, building a crowdsourced linguistic map.
- **Timeline layering**: Visualize how languages diverged over centuries, possibly layering historical events.

We hope this project inspires curiosity about the words we use every day and the rich tapestry of languages that shaped them!
