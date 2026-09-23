SIG: GenAI SIG
Date: 2026-09-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Felix Becker (Anthropic)** 01:05 Good morning.
**Tammy Baylis** 01:11 Hey, good morning!
**Siri Varma** 01:13 Good morning.
**Felix Becker (Anthropic)** 02:22 How's everyone today?
**Tammy Baylis** 02:30 Yeah, good. What's new with you, Felix?
**Felix Becker (Anthropic)** 02:34 How much?
I missed out on a few of these in the past weeks, because I was traveling, but…
**Tammy Baylis** 02:42 Welcome back.
**Felix Becker (Anthropic)** 02:44 Thank you.
**Tammy Baylis** 02:47 I suspect, the people who usually run this meeting might still be in a different one, would be my guess.
**Felix Becker (Anthropic)** 02:57 Who, who does run it, usually?
**Tammy Baylis** 03:00 Trask or Ludmila, or maybe Aaron! Hi, Erin!
**Aaron Abbott (Google LLC)** 03:05 Hey.
Yeah, I can hear… I think Trask will probably show up in a couple minutes, but… oh, there's Trask.
Anyway, I'm happy to share, let me…
**Tammy Baylis** 03:16 Oh, thank you. Trask.
**Trask Stalnaker (Microsoft Corporation)** 03:19 A,
**Aaron Abbott (Google LLC)** 03:25 Alright, is everyone able to see?
**Trask Stalnaker (Microsoft Corporation)** 03:30 Yeah.
**Aaron Abbott (Google LLC)** 03:36 We just had Felix's topic. Trask, did you want to say… I missed the… the morning APAC call, did you want to say anything about this one?
**Trask Stalnaker (Microsoft Corporation)** 03:46 No, I think we're good. Steve is interested in that PR also, and so he's gonna review and approve it, hopefully.
**Aaron Abbott (Google LLC)** 03:59 Cool. Well, I guess in that case, Felix, do you want to, talk about… I think we discussed this briefly in the other call, but… Feedback about… Otherwise.
**Felix Becker (Anthropic)** 04:12 Yeah.
**Aaron Abbott (Google LLC)** 04:12 4 goals, yeah.
**Felix Becker (Anthropic)** 04:14 Sure. I… so I promised to file some GitHub issues, I didn't get around to, but I found one. So this is something we ran into, probably, the biggest problem. The spec currently says that for… tool results, in two different places, it names a different type. So in one place, it says it can be any object, and in another place, it says it has to be an object in the JSON schema.
And then it says it must comply to the JSON schema. The problem is that, as far as I know, all AI providers, like both Anthropic and OpenAI, return a content, like, message block array. And so an array is not an object, and so… We don't know how to, fit that into this type.
And there was also a note that said something like, if it is, an object, or if it's a string, it should, like, the instrumentation should try to make it an object, so I also wasn't sure if this was supposed to be interpreted as, like, we should look inside of the… first text block and identify, is there a JSON string inside of the text block, and then put the object to that JSON string.
But that could also still be a JSON array, so that would then still also not be… Compliant.
So… my suggestion here would be, I think, the best thing to do would be to actually specify that it is like, a content part array, because I would allow both both, like, JSON content, but also tool calls that just return strings or, you know, non-JSON content.
But… in any way, I think it would just be good to specify, like, what the type actually is, and to resolve the contradiction between the two places in the spec.
Does that make sense?
**Aaron Abbott (Google LLC)** 06:22 Absolutely.
Definitely agree on the contradiction. I… I'm trying to pull this up, In the spec, so this is for… I'm curious, like, because you mentioned it's for providers, But this is, like, the execute tool spin, which is more of, like, an agent taking an action, right?
Did you mean in the context of, like, the data model of… the, like, cloud manifestations, or Cloud Code or something like that, or in the context of the inference.
**Felix Becker (Anthropic)** 06:51 Well, the, no matter where it's executed, right? Like, so, we do have… like, we're trying to add native support into Anthropic, so maybe we're, like, running into some of these a bit more strongly, but even if you're writing an instrumentation on the client side, right, when you execute the tool, that produces a tool result off the content like, array, because that's what needs to be passed back.
Into the, like, inference call, into the… chat completions, or responses API, or messages API.
So that's the… and I think if you look at the existing instrumentations for OpenAI and Anthropic, they… I think some of them just actually put the array inside of it, so they're technically already not compliant with what the spec says, at least in the JSON schema.
**Aaron Abbott (Google LLC)** 07:52 I see.
Yeah, I mean, do you have… I see the suggested changes, change it to content partner, right? I guess… I'm trying to think what we have for the Gemini API.
That it's… not a content part array. It just allows, maybe, like, a part above any or something like that. I would need to double-check, but… Yeah.
**Felix Becker (Anthropic)** 08:30 Yeah, I mean, definitely want to make sure that this works for all. I was trying to basically suggest the lowest common denominator, because my thinking was, like, if it's content par, then you can still put JSON inside of the text array, which is how tools are, like, modeled. Like, most tools do it that way in an AI and anthropic world.
Versus if you say it has to be, like, the… JSON result object, then it's unclear what to do when the, like, tool result is not, It's not, that form of content. It could even be, like, an image or a document, but I think instrumentations don't… those into Optel, generally.
Actually, I just… had Cloud add a sector into this issue, if you want to reload with, like, what all the existing,
**Aaron Abbott (Google LLC)** 09:29 Yeah, I think I saw that just pop up.
**Felix Becker (Anthropic)** 09:32 all the existing… Instrumentations do.
**Aaron Abbott (Google LLC)** 09:45 I… I see what you're saying, do you, you know…
**Felix Becker (Anthropic)** 09:51 Oh, you're muted.
**Dylan Russell** 09:53 Yeah, one weird case is the Google GenAI SDK, which lets you, like.
pass, like, Python functions, which can return anything.
Including, like, Python objects.
**Felix Becker (Anthropic)** 10:08 And then how does it serialize that for the API?
**Dylan Russell** 10:11 Edge case that maybe we shouldn't worry too much about.
**Felix Becker (Anthropic)** 10:15 How does it serialize that to the API?
You mute it.
**Dylan Russell** 10:25 Sorry, can you say that again?
**Felix Becker (Anthropic)** 10:28 How does it serialize, like, an arbitrary Python object to the API? Because the API then still needs to get, like, JSON or something, right?
You're muted.
**Dylan Russell** 10:45 Yeah, sorry, I was thinking. I think… I think you're… you're right about that, yeah. I… They must serialize the function to a… to some, like, JSON or… Proto thing, yeah.
**Felix Becker (Anthropic)** 11:05 I think the most, like… the… the best thing would probably be to, like, follow, kind of, the EPI types, and so… the API types… I haven't looked at, at the Google's, Google's API. Would be good to really confirm whether that's a content part array, too, or if that's, like a JSON object. But… one solution to that would be to add, like, a spec text that says, like, if it's… if the API is just a JSON object, like, serialize it into a text content part.
**Dylan Russell** 11:52 Yeah, that makes sense to me.
**Felix Becker (Anthropic)** 12:03 That's the… so just… that's the solution of, like, changing this type to a content part array.
of consensus.
So I could put up a PR.
**Aaron Abbott (Google LLC)** 12:17 Yeah, I just… so I just shared, like, in the chat, I'll also pasted in the issue, but in Google, the way we model it is this struct, which I think would be roughly equivalent to just, like, in any… it doesn't allow bytes, but it would be roughly equivalent to, like, any in JSON schema.
I mean, I can look at how it's converted to JSON schema, but… It's not, like, the content part, so specifically it doesn't have any structure, it's just, blob of data. It's just like a… It has structure, but it doesn't have any known keys, I guess is what I'm trying to say. Makes sense.
**Felix Becker (Anthropic)** 12:51 So it's my… yeah.
**Aaron Abbott (Google LLC)** 12:55 Yep.
I mean, I… I do see what you're saying.
**Felix Becker (Anthropic)** 12:58 They'll be happy with the content part error?
**Aaron Abbott (Google LLC)** 13:04 So, like, in the case of content part array, it doesn't have… arbitrary, structured data, right?
**Felix Becker (Anthropic)** 13:13 Why would we reuse the, like, content part, message types, and then… If the tool just returns, like, a JSON string, that would be, like, JSON stringified into one text content part.
**Aaron Abbott (Google LLC)** 13:33 Yeah, I mean, I think that's the difference, is that this… this is… like a JSON directly in the payload verse.
embedding a JSON string inside of the payload, which was escaped, yeah.
Does that make sense?
**Felix Becker (Anthropic)** 13:46 Yeah.
Yeah, I'm just… what I'm thinking about is basically, like, the consumers of this, right? Like.
somebody like Langchain, or, Datadog, or, like, Sentry, they'll want to render this pretty in the UI.
And so, for them, it would be important to know, like, is this just an arbitrary JSON object? In which case, I would just render, like, a, you know, pretty printed JSON, or some, like, JSON tree UI?
But then it would be a little weird if some instrumentations do have to use content part, because then you get this, like.
you're just, like, exploring the content part area.
Versus if we say, it's always a content part area.
then it knows exactly what to expect. It can reuse the content part renderer that they already have for, like, the other message types.
And maybe they could still detect if, like, there's JSON inside of a text block, and extract that too.
But if we say it's just any.
You can't really assume anything, because… Even instrumentation such as put a content part array inside.
That could have just been the tool… Result, like, the tool returning that particular type, so you can't really make any assumptions.
**Aaron Abbott (Google LLC)** 15:16 Yeah, but if it's a JSON string, like, you have the same problem, right?
It's just a… you would render a string with the JSON.
**Felix Becker (Anthropic)** 15:28 yeah.
Which is, I mean, that's just… in, I guess, all the non-Google APIs, that's just what they, like, how the APIs work.
**Aaron Abbott (Google LLC)** 15:40 Yeah, no, I hear you. I'll take a look at the other ones. I still… I'm still slightly confused, because I feel like we're talking about inference APIs, so, like, when you feed the dual call response back To, say, like, anthropic or, you know, at the model level, but… At the content… at the level of, like, the frameworks, I see… I see you left some stuff here, so maybe we can… we can dig into it a little more, but, like.
I think… at least, at least, Trying to think what LaneChain does.
I feel like you can return just, like, Python object, and at the level of the framework doesn't care if it's content array or not. Like, it would just respect whatever's returned from it, but… No, I think… I think I can do… I can do a little reading offline as well, and we can…
**Felix Becker (Anthropic)** 16:31 Yeah.
Well, the minimum asset I'd have here is to… to remove the contradiction, so that it doesn't say object and any in the other place, because that really puts, like, a… like, some instrumentation's actually violated, and then others, I'm like… Should I just nest it under, like, a content key that then has the array?
Yeah, so just… I want to be consistent with that.
By now, for our instrumentation, we've, because I don't want to, like, break anyone until this is decided, I just put it on, like, an anthropic.tool result property.
But once… We've specified this, I can move it to, like, the actual… attribute.
**Aaron Abbott (Google LLC)** 17:20 Yep.
That definitely makes sense.
Anybody else have some thoughts on this one?
**Emil F** 17:31 I think that in Langsmith, we're just, rendering that as a JSON, like we are expecting a JSON to walk.
**Trask Stalnaker (Microsoft Corporation)** 17:46 Felix, could you… oh, go ahead.
**Felix Becker (Anthropic)** 17:49 You, you go ahead.
**Trask Stalnaker (Microsoft Corporation)** 17:52 I had a… Separate question.
**Felix Becker (Anthropic)** 17:59 Yeah, I don't… I don't really have a question.
**Trask Stalnaker (Microsoft Corporation)** 18:05 Oh, maybe related. The, comparing any… to… The content art array.
I think you s… Can you explain your… the preference for content part array versus any?
**Felix Becker (Anthropic)** 18:26 yeah, I mean, this is… This is what, this is how the, like, Anthropic API, the Messages API, and the OpenAI APIs work, so… tool AI's… tool results, Or reuse the same, like, content… Block messages, as, like, messages themselves, like, output and input from the model.
Because if you think about it, like, the tool result at the end of the day has to go to the model. It has to go to an LLM, which only understands certain types of content, right? It understands text, it understands images, it understands documents.
And so… that is why these APIs are modeled that way. And, Not… like, there are tools out there that make use of that, so a tool can choose to return a JSON string that puts inside of a text block.
But it can also choose to return an image, it can also choose to return just a document, it can choose to return, like, an XML string inside of the text block.
By using, like, the content parts.
I think you're, like, you're more clearly specifying what the shape should be, and then you can specify, like, how… if you… if there is a provider that, like, oh, it just accepts any directly, like, you can specify, oh, like, JSON string, if I put it in the text block, whereas if you make it any.
It wouldn't be clear for me, like.
how I'm supposed to take my content block array and put it in there. I guess we could also specify just JSON stringify your content block array.
And put it in. But then, I would imagine that that's worse for the UI that's trying to render this, because it cannot, like, reuse the same content part renderer That they use for… like, the GenAI dot… Messages pokerty.
And then there's also the question of, like, if I'm a… if I'm a specific provider, like, anthropic.
would I then actually put my native response types into there, like my native content block arrays, or do I use the GenAI content part arrays, like, I translated to that.
So I just, I feel like if you just set it to any, it leaves, like, the spectrum of, like, the possible values much more open.
**Trask Stalnaker (Microsoft Corporation)** 21:16 Cool. Thanks.
**Aaron Abbott (Google LLC)** 21:18 Yeah, that helps, Felix, thank you. I'll take a look at this one.
Offline as well.
**Felix Becker (Anthropic)** 21:31 Thank you.
**Aaron Abbott (Google LLC)** 21:32 Cool. I guess we'll move on to the next one.
Ankit, are you around?
**Trask Stalnaker (Microsoft Corporation)** 21:51 I don't see him on the call.
**Aaron Abbott (Google LLC)** 21:54 Yo.
Does anybody… did anybody add this that wasn't on kit?
Alright.
Well, we had a shortage on it today, probably because of the stabilization stuff we're working on. If anybody… also something they want to discuss. I also see a couple new people, if anybody… I mean, no pressure, but if anybody wants to… Introduce themself, I'm gonna share the meeting doc here as well in the chat.
But, yeah.
**sallyann** 22:39 Hey, sorry, I'm new here. Happy to get your intro, did you want me to write something in the doc, or just talk here?
**Aaron Abbott (Google LLC)** 22:44 Oh, no, no, you're welcome to just talk, I meant, if anybody wanted to add agenda items, but yeah, nice to meet you.
**sallyann** 22:50 Cool, yeah, I'm sallyann, I'm head of product here at Arise. Just wanted to kind of jump in. We also have Chip here from Arise. I don't know if you've already intro'd yourself, Chip, but we'll just kind of be… be joining here. We work a lot on the observability, tracing side, open inference side here at Rise, so I just wanted to join these conversations.
**Aaron Abbott (Google LLC)** 23:08 Awesome. Nice to see y'all.
Okay.
What do you think, Trask? Should we call it early?
**Felix Becker (Anthropic)** 23:20 I couldn't talk about a few more things, if we have time.
**Trask Stalnaker (Microsoft Corporation)** 23:27 Sure.
**Aaron Abbott (Google LLC)** 23:28 try her.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 23:28 Yeah, I also had… I was also gonna put in an agenda item, sorry I joined late. But yeah, if Felix wants to go ahead, yeah.
**Felix Becker (Anthropic)** 23:39 Okay, one, this is a little smaller, Currently, finish reasons is not typed.
Like, there's… they used to be an enum, I think, and then it was changed to just a string array.
And, openAI and Anthropic have… Similar values that are, like, half equivalents to each other, but they're not the same.
And so… I don't really want to put, like, just our vendor-specific values in there, and then have them not match. I looked at the… like, existing instrumentation for Anthropic or OpenAI, and one of them, I think, actually, like, I think the Anthropic one actually normalizes it to whatever the OpenAI one does.
But it's, like, not specified what the values should be.
I'm curious why… this was changed to a string array, and if we can maybe change it back again to have, like, specified values, because I imagine it's not… Not very useful for readers if, like, they can't match attributes across different vendors.
**Aaron Abbott (Google LLC)** 24:55 Yeah, I think… So I'm trying to see where it's deprecated, and I also was just gonna call out, it's in two places, so it's also, like, normalized into the spans out of the, response body, so you… so I'm trying to find that one really fast, but… Does anybody remember why we did this?
So it's here also, and then… See if I can find it.
**Felix Becker (Anthropic)** 25:34 Also, just added the section again for… What existing instrumentation still?
**Aaron Abbott (Google LLC)** 25:40 Yup.
Yeah, my hunch is that it was difficult to normalize across all the providers. I think, like you mentioned, Felix, it's… So, easy to do for OpenAI and Anthropic, I think.
We could probably define… Like, a mapping up front.
Yeah, could you say… maybe say more also about the use case for the normalization? Because I know this is always a tough topic.
**Felix Becker (Anthropic)** 26:10 Well, my, my thinking is, like.
I have two options as an implementer, right? I can either emit… the… stop reason as, like, a custom vendor prefix attribute, or I can use the GenAI attribute, and I'm imagining the benefit of emitting a GenAI attribute is that any consumer can build, like.
dashboards or filter queries, or build… like, platforms can build UIs that render things in a standardized manner.
If the value is not standardized, though, I don't really see the benefit of having the attribute at all.
Because it would be kind of better to just do a vendor prefix property, since it's a vendor-specific vocabulary.
**Trask Stalnaker (Microsoft Corporation)** 26:59 There can still be, benefit to having a common attribute, because dashboards, like, common dashboards can still incorporate that.
And it can still, you know, be displayed and, But yeah, we have, there's a few places in semantic conventions where we have kind of that Conflict of, like, sometimes, there's a normalized version and a free-form version.
But I don't remember what the… Balancing act here was.
**Felix Becker (Anthropic)** 27:38 Yeah, so would you say I should just emit it with our, like, vendor-specific values, or should I try to map… to, like, whatever OpenAI does, which is what, like, the instrumentations currently do. There's, like, a… The mapping and the code.
My worry was a bit that, like, you know, before bringing this up, that, like, if we were to change this, then I'm breaking consumers after, if we have to change the values.
So I wasn't emitting it for now.
**Trask Stalnaker (Microsoft Corporation)** 28:16 I, I think from… For following semantic conventions, you would, like, you would emit it.
here in the GenAI attribute, Since it doesn't look like we have any guided, like, any normalization, it's just… You could… we could add… We have vendor-specific, sections in semantic conventions.
Where we could, document the specific values that Anthropic, for example.
emits… If we wanted to encode that into the specification, as far as, you know, breaking, yeah, like, I mean, if we… Happened to change it between now and when we mark it as stable.
you know, that could propagate breaking changes onto your consumers, so, I mean, that's… a risk of adopting any of the current GenAI stuff.
**Felix Becker (Anthropic)** 29:35 Okay.
So, like, for now, there… you know, you would prefer to just keep it, Keep it, like, an open… Like, arbitrary string array.
That's vendor-specific.
**Trask Stalnaker (Microsoft Corporation)** 29:52 I'm not sure I have a… I don't know, I'd have to look at why… the history there, see why we changed it.
And I would… Yeah.
I mean, it is definitely a good question. It's a common question in semantic conventions of whether to normalize things or emit the values that are actually sent by the provider. There's, you know, obviously pluses and minuses to both there.
**Felix Becker (Anthropic)** 30:26 Yeah.
I… I was thinking maybe it would be valuable to just standardize, like, a few very common properties, because they're… Just looking at what existing instrumentations do, there are just, like, these, like.
very equivalent, but slightly different values, like tool use, or tool call, or, like, max tokens, or length, or… refusal or content filter that, like, they're the same semantically, but they're just, like, a slightly different… wording, where we could just, like, define one for those cases, and maybe leave the The rest open, still?
**Trask Stalnaker (Microsoft Corporation)** 31:10 Yeah, totally.
**Aaron Abbott (Google LLC)** 31:14 Yeah, and I feel like that's what we had before. I feel like we had a couple well-known values, and then, like, enums are open in semantic dimensions, as far as I understand, so it would be, possible to add your own, and then I could have sworn we had the specific subunume, like a specific specialization for OpenAI, but… Yeah, plus one to know what Trask said, maybe we should spelunk the code a little and see, why it was removed, like you mentioned, Felix, it was deprecated at some point.
**Felix Becker (Anthropic)** 31:43 There's maybe a little bit of a separate topic.
**Trask Stalnaker (Microsoft Corporation)** 31:44 Very… sounds like a very reasonable… Proposal.
On its face value, yeah.
**Felix Becker (Anthropic)** 31:51 Like, in general, when there are vendor-specific values or attributes. I wondered if the spec should have some kind of standardized way to prefix them?
So that… because I'm always worried about, like, if I emit a value, and then later the spec Changes to actually introduce a native concept of that, and it has, like, a slightly different schema.
now we're in conflict. So, like, here in Finnish Reasons, we could say there's a… specific vocabulary, and then anything else, you bender prefix, so that it would be, like, anthropic underscore refusal, if that's, like, a custom one. So that if you later introduce your own refusal with a specified meaning.
that is, like, it doesn't conflict between the two. I think more is this a problem with, like, the content types and the content parts, where we say, like, you can have a generic part that can have any type discriminator value.
But… if, let's say, I emit a type image right now, and then tomorrow the GenAI conventions start defining their own type image, and I chose a different schema for my type image than the conventions.
UIs, which is, like, Kind of break, or not know what to do with their values.
And it might be better if I emit, like, anthropic underscore image.
And we say, like, every generic part should always be vendor prefix, so that we reserve the ability to evolve the schema over time.
**Trask Stalnaker (Microsoft Corporation)** 33:39 Possible, that's why we didn't reserve, like, certain names.
Trying to think of… In other semantic conventions where we've had this and we decide to… I know in, like, messaging and database for, like, database operation name, like, it's select, or update, or… but we don't normalize that anywhere. We just say provide, you know, whatever the database… the vendor calls that operation.
And… It's honestly been fine, like, like, from a dashboard perspective, it gets… Kind of… Naturally grouped, and there's not a ton of… I don't know, but I also know that there's a lot more… People are doing a lot… want to do a lot more calculations and things on the GenAI data today.
**Felix Becker (Anthropic)** 34:39 Sorry, what is the database example? Can you explain that more?
**Trask Stalnaker (Microsoft Corporation)** 34:43 Yeah, so, like, operation name, for databases, like, it could be select, insert, update, delete, select, you know, your typical CRED operations.
But we don't actually define that anywhere. We say to use whatever the, database vocabulary is. Just capture it, whatever the database uses.
So we don't try to normalize… In a lot of cases, messaging, we have similar, like, different… people have different terminology for settling a message, acting it, knacking it, And we say, you know, use the… vendors, terminology. We don't try to… But then, sometimes we do have a… another attribute.
Which will categorize, kind of, specific things that we want, so… That's another option if… Like, I think I've resolved… The finished reason, like, it's… It's a bit like a status, like, it's your… like, you're… Response code, your status, like, there's…
**Felix Becker (Anthropic)** 36:04 Yeah, I mean, I can see it for a finished reason. It's like, well, if it's refusal, it probably means refusal, right? Like, there's not that big of a… difference. I think, I was more, way more thinking about, like, all the content parts, About, like, the potential for breakage there, because I imagine platforms are actually building UIs on top of those JSON structs.
And then… if they have different schemas in the future, the UI just… Wouldn't know how to handle it.
**Trask Stalnaker (Microsoft Corporation)** 36:43 Just a close… last thought on the finish reason was that, I mean, if we have vendor… if it's just, you know, supply whatever the vendor wants for now, we can always add in or overlay, like, a finish reason type.
Something that's, like, another attribute that is a more strict enum, like success, failure, canceled, you know, some… some basic…
**Aaron Abbott (Google LLC)** 37:18 Yep. I was… I think I was just gonna call out, Felix, I think you're mostly talking about the structured, like, JSON schemas for top-level, like, span attributes and such. We do have, like, this prefixing, so this is, for example, like, in the OpenAI one,
**Felix Becker (Anthropic)** 37:34 Oh, really?
Yeah, are you showing up right now?
**Aaron Abbott (Google LLC)** 37:38 Yeah, it should be.
share it.
**Felix Becker (Anthropic)** 37:43 I just see, like, the request top K page.
**Aaron Abbott (Google LLC)** 37:48 Let me start over.
**Felix Becker (Anthropic)** 37:51 We are sharing a different tab.
**Aaron Abbott (Google LLC)** 37:54 Yeah.
I think it's this one.
Can you see, this right here?
**Neil Yashinsky** 38:01 Yeah, OpenAI request service tier.
**Felix Becker (Anthropic)** 38:03 Oh, okay, yes.
**Aaron Abbott (Google LLC)** 38:05 Oh, sorry, I was sharing the right thing. Yeah, so I can share this in chat. So this is, like, OpenAI specializes the inference band, but we don't have anything like this for the JSON schemas, and… I think it would be pretty clunky to have keys with dots in them in JSON, to be honest.
It's a- it would be fine, but…
**Felix Becker (Anthropic)** 38:25 Oh yeah, I was… I was… I was gonna use underscores, not dots. Yeah, yeah.
**Aaron Abbott (Google LLC)** 38:29 Yeah, that's my takeaway, though, is, like, we should figure out how to… Like, when you have non… when you have open types, it's kind of easy to accidentally make breaking changes, because people could put Different stuff in there at some point, so… Yeah, I hear you.
And I also filed… this… I'm filing a couple issues for the JSON schemas.
Here.
**Felix Becker (Anthropic)** 38:59 Yeah, like, to maybe… talk about, like, a very concrete example, and I'd love to get your guidance on, like, how I should represent that, like… we have a bunch of content that's not specified in GenAI, right? Like, we have images, we have documents, we have, search results for our, like.
Tool search tools for, web search tools.
And we also have, like, MCP tool calls, where there's, like, extra attributes, like, we have the MCP server name.
And then… so, I was thinking, like, do I just filter those out, not show them entirely? Do I report them just as, like.
Say, type search results, or type image.
Or do I report them as, like, type anthropic underscore image, type anthropic underscore search results? And similarly for, like, if I want to add the MCP server name to a tool call, do I put that as, like, MCP server name, just as an attribute on the existing standard type?
Or do I put Anthropic underscore MCP server name?
yeah, curious what, like, how you would… Recommend implementing, or, like, what the intent is.
Because there are, like, additional properties are explicitly allowed in the JSON schema, and there's the generic part definition.
**Aaron Abbott (Google LLC)** 40:35 Neil, you wanna go ahead?
**Neil Yashinsky** 40:37 Yeah, thanks. So, Trask and I may have mentioned this once before, I may have some, useful, data to provide, like, how this works in a real-world example. So, as I mentioned, I think it was two weeks ago, that, We've been working on a new benchmark across models, and as we looked closer at this, it seems like, we could provide what I like to call a reference instantiation, which is, like, how this works, at least in one real-world example across Only 3 of the vendors, but across OpenAI, Anthropica, and Google, same task.
And so it, you know, provides a living example of how and where this, at least in our experience, you know, works well or doesn't.
And so, it's the… just the very, end of the, like, the final tweaks and configurations around the models themselves. But that's actually what's interesting, is because the… the configuration is… not static across them. It's optimized for each of the model's performances. You have one task, and three different models' data… you know, their data structures, and then a real-world attempt to merge them into a single OTEL-compliant… you know, semantic convention, stabilized, what have you, data structure, data scheme.
So, a little, a little early to show real-world examples, but probably by next week at this time, I could show, you know, a specific instance, how it looks, etc, so people could have a fleshed-out example.
I think that was Felix is… what you're kind of looking for, yes, Felix?
If I heard right?
**Felix Becker (Anthropic)** 42:25 Sorry, what?
**Neil Yashinsky** 42:26 For example.
**Felix Becker (Anthropic)** 42:27 I was looking for what?
**Neil Yashinsky** 42:29 I thought someone mentioned, looking for having, like, a tangible, real-world example of how this looks for, you know, real model calls across, you know, the differing, existing schemas, and how they merge together under the new semantic conventions.
**Felix Becker (Anthropic)** 42:44 Sorry, I was… I was trying to give an example of, like.
where, in practice, I wasn't sure how to represent, like, whether to, like, render prefix something or not.
**Neil Yashinsky** 42:58 Yeah, I don't know if it'll… if it'll… it'll provide exactly what you were looking for, but it might provide some of the… You know, examples around Anthropics.
**Felix Becker (Anthropic)** 43:07 Specific.
**Neil Yashinsky** 43:07 like, data, and how I capture it and unify it.
**Felix Becker (Anthropic)** 43:12 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 43:16 For, for the content type, for… The… it does… My initial reaction to it would be… To prefix… custom… schema… part, like… schema stuff.
I feel like that's the most natural way to be like, hey, this is… I mean, the whole point of semantic conventions is to have these schemas, whether it's at attribute level or a JSON level.
**Felix Becker (Anthropic)** 43:55 Exactly.
**Trask Stalnaker (Microsoft Corporation)** 43:56 That's how we do it at the attribute level, prefixing stuff, so… I feel like that feels natural at the JSON schema level.
**Felix Becker (Anthropic)** 44:12 Which I do think is what I'm different.
**Trask Stalnaker (Microsoft Corporation)** 44:15 I do think it's different from the Finnish reasons discussion.
**Felix Becker (Anthropic)** 44:19 Yeah.
I can see that. I think the messages part, like, to my understanding, I don't… I'm not even aware of any other OpenTelemetry conventions, right, that, like, go this deep on specifying JSON schemas for the attributes, and…
**Aaron Abbott (Google LLC)** 44:35 Yeah.
**Felix Becker (Anthropic)** 44:36 I think these are used in, like, way more programmatic manners, maybe, than other OpenTelemetry conventions, like… you know, platforms like Bring Trust, they ingest the messages, and then they allow you to write evals on top of them, and, like, people write graders and assert on the content, and so, like, there's a lot of programmatic code being written That assumes certain standards, and then… I feel like the… not having, like, conflicting types between discriminators becomes a lot more important.
**Aaron Abbott (Google LLC)** 45:10 Maybe if I could make a suggestion, like, what if we just had people come in, like, we allow additional right now, which is fine, we could continue to do that, but what if we let people, you know, add stuff to the schema in the hotel semantic conventions with the prefixes? Would that be… I feel like it would be helpful to actually For us to make sure we're not introducing breaking changes by defining stuff later, and it would just be… easy, but I don't know, Trask is that something… it'd be a little bit different where we usually have, like, the OpenAI thing I showed.
What do you think?
**Trask Stalnaker (Microsoft Corporation)** 45:48 I don't have a super great grasp on it, But the… the core… I mean, anything that we put in semantic conventions wouldn't necessarily have to be prefixed.
Because we own it, and we can control, sort of, that… The overlap.
But anything that vendors… Add, additionally.
Would be prefixed, but in that case, it probably would make sense to go ahead and prefix… If we, where we have the vendor-specific semantic conventions, like the OpenAI or Anthropic-specific stuff, we could… Prefix those… Type.
Somehow we need to have… Separate schemas, separate JSON schema. Somehow we need to have valid, dateable, or real JSON schemas.
And allow… and also allowing this… the federated kind of concept.
Where people can… Control their own stuff, overlay their own stuff on top of the core semantic conventions.
I'm not… I don't think I have a good enough grasp on it, Say how that best accomplished that.
**Aaron Abbott (Google LLC)** 47:20 Yeah, I agree with the end result, though, for sure. Just figure out the best way to do this kind of thing.
**Felix Becker (Anthropic)** 47:27 Yeah, if we have rough consensus on this, I could put up a PR to just add, like, the… prefixing to the spec text, and I would… Supply.
**Iwa Wong** 47:39 One thing to share, though, from the consumer side of things, so this is, Iwa from, A company that, correlates this data, where we are trying to, detect financial, road agents, where they're trying to do money laundering and whatnot. Some of these financial agents, financial institutions, they may use, like, say, Google's, versions of, the response API, or, like, Intropic OpenAI, right?
But because of how these malicious factors are actually, hiding their things. We need a way to actually correlate these data across vendors.
So I think, to Felix point, I think we need some kind of, like, common, set of attributes, that is common across vendors.
Just so that we can know, like, we're comparing apples to apples, you know what I mean? Because, like, if we're having, like, too many custom, vendor custom, fields without a mechanism to review periodically, hey, like, are we actually, are we actually saying the same thing, but just named differently? Miss, like, downstream, things, for example, like, abuse, security, or all these other, finding bad, that's really hard, because we don't know, like, when we're looking at a vendor-specific attribute, like, does it actually mean something else in, like, Google, OpenAI, whatnot?
**Aaron Abbott (Google LLC)** 49:17 Yep.
No, I think… I think I agree. I don't want to speak for everyone, but the… Like, if somebody introduces something at first.
and other providers don't have it, it'd be nice if they have, like, a place to put it and some kind of guarantee that it doesn't get broken later. Like, I think, Felix… the frame of your question was, what happens when we do add it to the semantic conventions? How do we make sure it doesn't conflict? So, like.
I think we all share probably the goal of having some normalization.
But then, maybe early on, it's… it's kind of tough, and we might need the, vendor-specific prefixes.
Oh yeah, I agree.
**Iwa Wong** 49:55 It's the correlatability that I worry about here.
like, whatever the team decides on, like, I think is good, but, like, I want to ensure that we have a way to correlate Amount vendors,
**Felix Becker (Anthropic)** 50:11 Yeah, like, the… The problem is that today the conventions allow any additional properties and any additional parts, right, without any prefixing. So the… Like, you have this problem today already.
Even if we don't prefix. I feel like the prefixing makes it, like, strictly safer.
**Iwa Wong** 50:38 I agree, it's safer, it's… But, like, we need a mechanism to… Be able to tie it back when… There are multiple prefix versions of vendor-specific attributes that actually mean the same thing.
**Felix Becker (Anthropic)** 50:54 Yeah.
Which, in the case of properties, you know, you could… you could double report them under both names. I think maybe with content parts, it gets a little trickier, because if you… double report them, now you're implying there's two of them, so, it's a little messy.
**Trask Stalnaker (Microsoft Corporation)** 51:16 Iwa, are you…
**Felix Becker (Anthropic)** 51:17 That's fine.
**Trask Stalnaker (Microsoft Corporation)** 51:18 Specifically, in talking about the finish reasons, or the content parts, or both.
**Iwa Wong** 51:26 Really both. Actually in general, when you think about these malicious actors, they could really, trick the LM to actually do malicious things.
So finish reasons is, one thing that is crucial, tool calls, how many cold calls are actually, using, what kind of tool calls are we, for what reason and why.
Some of these, MCP calls, like, could also be, malicious, or change under the hood. So having something in common across vendors can actually, like, help, catching these malicious actors, or actually cross-vendoring, cross-platforms.
That's what we're seeing on the financial side of things, like some of these, agents are actually doing money laundering and things like that, so I just want to make sure that we have a way to correlate and compare apples to apples.
**Trask Stalnaker (Microsoft Corporation)** 52:22 So, certainly, I mean, that, that is… Right? One of the big objectives of the semantic conventions overall is to, unify things, And the reason I ask, I think there's kind of different discussions… different discussions around the finish reasons versus the content parts. The content parts, I feel like, is more… Follows, our very even though it's JSON schema, I think it follows the semantic conventions, what we've done in the past of, like, if you look at database semantic conventions, we have, you know, MySQL, Postgres, we've got a bunch of vendor-specific things, Redis, and we're… Where they're unique, they're there, but at some point, you know, when we see… when we do see commonality, right, we pull that up a level to kind of the core database semantic conventions, even if it's only a General concept that's adopted by a few database servers, so that you can have that correlatability.
And so, I see the content part stuff similar, the JSON schema stuff, similar to that.
Where… You know, if it's only anthropic, you know.
Sure, we should, you know, if it's unique to them, it should just be under their prefix.
As we see… and, you know, and that can change over time, right? And that's what major version bumps are for. Also, we can bring common things up a level in… and have that correlatability And… You know, figure out a way to deprecate, you know, vendor-specific stuff over time.
The finish reasons… is… tough, discussion, and that's where, like, I think I kind of… my initial, at least for what we've done elsewhere in semantic conventions, the most… the clearest mapping to me would be, finish reasons would be, like, whatever the vendor sends, their vendor terminology.
And if we do need want correlatability, maybe a finish reasons type.
Which is, an enum of things that sort of group those, reasons.
But I also, you know, we would need to look at what the history there was. Maybe we can go back to Finnish Reasons being a… just an enum. I'm not… I'm not sure there.
**Iwa Wong** 55:13 Yep, whatever the team here aligns on and decides, works for the team that's good, I just care about whether I can correlate them or not. That's it.
**Emil F** 55:27 Well, I think that the whole Finnish reasons discussion is the easier one, because all the LLMs are emitting Finnish reasons in one form or another, and If there is a convention that says these are the, these are the allowed strings, even if it's left open-ended, you can add more to them.
then any new implementation will take a look at that convention and would tend to stick to the Finnish reasons that are already defined. Because right now, everybody… there is no Finnish reasons defined, and everybody's inventing their own.
**Iwa Wong** 56:05 Yeah, that makes a lot of sense.
**Trask Stalnaker (Microsoft Corporation)** 56:09 Yeah, it would be great if somebody want… somebody can kind of research the history there, and of why we switched and maybe present… make a… a concrete proposal there for how to… what… what would make more sense for finish reasons.
**Iwa Wong** 56:38 not to shuffle things on your plate, Felix, like, since Anthropic has, thoughts about for negotiations, like, would you be taking that on, or…
**Felix Becker (Anthropic)** 56:50 Take on what exactly, like, making a proposal for standardizing Finnish reasons?
**Iwa Wong** 57:02 That's my understanding.
**Felix Becker (Anthropic)** 57:04 I could do that, if there's, interest.
I wasn't sure if… if the interest on finished reasons was… Like, strong in the room.
Yeah, I mean, I think it's worth it.
**Trask Stalnaker (Microsoft Corporation)** 57:19 Exploring.
**Felix Becker (Anthropic)** 57:20 Okay, I can put up a PR maybe to, to just… Try to find, like, a common… like… Denominator set that, like, most of the providers do have.
So we have one vocabulary, and we could still leave the enum open for other values.
**Trask Stalnaker (Microsoft Corporation)** 57:44 Yeah, if you could also check just the history, since it sounds like, we… Flip-flopped that.
**Felix Becker (Anthropic)** 57:53 Maybe.
**Trask Stalnaker (Microsoft Corporation)** 57:54 See what the reasoning was there, if that's something that, still makes sense or is addressable in a different way.
Or… or we just want to change our, prioritization of, you know, we want normalization over… is more important to us than whatever reason it was that we… flipped that.
**Felix Becker (Anthropic)** 58:16 Yeah, okay.
**Aaron Abbott (Google LLC)** 58:21 Awesome, and just a reminder, this one, I guess, would… is part of inference, so it would be in scope for the stabilization, so it seems high priority to me.
**Trask Stalnaker (Microsoft Corporation)** 58:31 Good point.
**Aaron Abbott (Google LLC)** 58:33 Cool. I know we didn't get to all the topics, I'm sorry, folks, We're just about at time, so… Unless anybody had something really quick, we should probably… Out there.
**Neil Yashinsky** 58:45 Sounds good, yeah. It was a productive session, I think.
**Trask Stalnaker (Microsoft Corporation)** 58:48 Yeah, both of those, topics are very, I think, are on the, the stabilization front, the content part stuff also, so… Thanks for bringing those up.
**Felix Becker (Anthropic)** 59:00 Yeah, and thanks for all the input. This is, very helpful to talk through.
So I'm working on the implementations.
There's a lot more of those topics where those came from.
**Neil Yashinsky** 59:12 Looking forward to it.
**Felix Becker (Anthropic)** 59:14 Cold. See you next week.
