SIG: LLM Semantic Convention WG
Date: 2025-09-23
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Minghui Zhang** 01:38 Hello?
**Liudmila Molkova** 01:53 Oh, hi. Sorry, my, my, Zoom didn't work. How are you?
**Minghui Zhang** 01:59 Yeah, fine.
Sorry for late, training, finding… finding a place to, for this meeting. It's very hard.
**Liudmila Molkova** 02:10 Oh, I'm sorry.
Yeah, thanks for joining.
Let me share my screen.
This is… Much time for you, Kui?
**Minghui Zhang** 02:39 Yeah? Sorry.
**Liudmila Molkova** 02:41 What, what, oh, what is the… I'm trying to figure out what time is for you.
**Minghui Zhang** 02:47 Yeah, I have noticed there are… the, You have discussed my topic, and I get my answer.
**Liudmila Molkova** 03:01 Oh, okay. Do you want to talk about something else?
**Minghui Zhang** 03:07 but you can see the agenda I have left for, yeah.
Let's talk about that.
**Liudmila Molkova** 03:27 Patrick, if he would like to introduce yourself, or if you.
**patrickpok** 03:33 Sure.
**Liudmila Molkova** 03:34 Anything to discuss, please go ahead, add things to the agenda.
**patrickpok** 03:37 Nothing really to discuss, so I'm going to leave for Minghue. So, my name is Patrick. I actually come from the Java SIG, so I'm, like, I'm a contributor of the OpenDelemetry Java.
Recently, we have a lot of work at my company, like, regarding AI, so it's my first time joining, just to a little bit catch up with what you guys are doing.
I don't have particular topics, so definitely the floor is for you guys.
**Liudmila Molkova** 04:03 Yeah, thanks for… go ahead.
**Minghui Zhang** 04:05 So, go ahead, I'm sorry.
**Liudmila Molkova** 04:09 I just wanted to say thank you for the intro. I'm Lyudmila, I work on GenAI semantic conventions and semantic conventions in general. Welcome to the group.
**patrickpok** 04:19 Happy to be here. Thank you, guys.
**Minghui Zhang** 04:21 Yeah, let me do a short introduction. I'm, Ming Huizhang from Alibaba Cloud and, in China. So, my work is, about, all about the.
Open telemetry and, observability, for our users.
We are… we are a cloud provider, for our… customers to give them the availability for the microservices and the, gene AI applications, and so on.
Happy, happy to, meet you, yeah.
**patrickpok** 05:09 Thank you so much.
**Liudmila Molkova** 05:15 Yeah, so…
**patrickpok** 05:17 I just have, like, a very short question before you guys, so… because it's my first time here, so I'm very sorry. So, what is, like, about… the LLM semantic convention, because, like, our company, we are obviously working with LLM like everybody does, so what is… so, do we… are you guys trying to bring observability when, like, they are training a model, or, like, while they are doing inference, or… Oh, well, like, I don't know what you guys are doing, if you can just…
**Liudmila Molkova** 05:48 Yeah, great question. So, the main goal, We have a project scope identified, defined here. Give me a sec… Shouldn't have.
The main goal is essentially inference, but… It also includes, let's say, agents.
And more complicated workflow. We have, some conventions that capture the… The model side, performance, and… there were… Some ideas to expand it further.
Actually, currently, we're mostly focused on inference and agents.
**patrickpok** 06:40 Okay, got it.
So, what is the end of this? Like, because I see LLM, so will I be able, like, one day… because… So, there is a lot of service providers, I mean, like, the cloud observability providers, that can always, also, like, I mean, already offer those kind of, like, chat with you metrics, chat-with-you observability. Is this what you guys are doing now?
**Liudmila Molkova** 07:04 Oh, no, actually, this is the observability into communications for ZellM, right? So you're, sending some messages to the model, the model generates something back. This… this is… we captured this interaction. I see.
**patrickpok** 07:19 Thank you so much, thank you so much.
**Liudmila Molkova** 07:20 Yeah.
**patrickpok** 07:21 But, like, I would say, like, on the model directly, not, for example, the observability of the HTTP call, or, like, the size of the token, or the byte size of the response back. You guys are really, like, the observability of the LLM model itself, am I correct?
**Liudmila Molkova** 07:38 No, no, no, we capture the client side, so… So imagine that you have an SDK, like OpenAI SDK, And if you look, let's see, into the semantic conventions we have… For example, this is the OpenAI span.
You would find, the information about the client call.
You would see, okay, this was a chat call, the model was this, the call ended with this outcome. It's not HTTP, right? Because it's level higher than HTTP.
You don't see those details on the HTTP level, right?
**patrickpok** 08:26 Got it.
**Minghui Zhang** 08:31 Yeah, parts,
**Liudmila Molkova** 08:34 That's it.
**Minghui Zhang** 08:34 as I know, some of logs in our SIG may, be, interest, interested in the, model-side, the survey side, the server side, instrumentation. So, for the VRM or SGLAN, we can also create the spans or the availabilities, the… We can also capture the data for all of them to give some availability for the model service, and what we are… one of my work is to, provide this, motorcycle.
observability. And if you are interested in it, we can give a more deeper, discussion.
**patrickpok** 09:27 Sure, definitely, but I mean, obviously, after your agenda.
**Minghui Zhang** 09:32 Oh, okay, yeah.
Poor.
**Liudmila Molkova** 09:38 That one's good.
Okay, Minku, do you want to present, or do you want me to present?
**Minghui Zhang** 09:46 Maybe you can present it, yeah.
**Liudmila Molkova** 09:50 Yeah, sure.
Okay, so you have a pull request for… for this.
**Minghui Zhang** 09:59 Yes, we have an inner employment of that set, and I just, move it to the… Open dynametry, semantic omissions.
**Liudmila Molkova** 10:14 Yeah, it's, it looks good. I think there are a couple of comments. I think Alex left a comment that It would be useful to update the, Jupyter notebook.
**Minghui Zhang** 10:28 Yeah, some of them, I have, replied it.
And, maybe we need a more discussion. So… the type of the tour is, it's hard to, give a definition, because, I have, I have, search, research about the, the implement… implementation of, OpenAI, cloud, DeepSeek, and our inner API, and I find that most of the, model, provider gives… just gives the function type.
And for OpenAI, they give the customer type for, a general… a generic, input, from, format. Or you can just, I'll add the link in the eye. Yeah.
**Liudmila Molkova** 11:40 Boy.
**Minghui Zhang** 11:41 So… maybe…
**Liudmila Molkova** 11:45 This is the created completion.
**Minghui Zhang** 11:47 Yeah.
**Liudmila Molkova** 11:54 What's your email?
**Minghui Zhang** 11:56 Here we have tours.
Yeah.
**Liudmila Molkova** 12:09 It's wild.
**Minghui Zhang** 12:10 So you would… Yeah, go ahead.
**Liudmila Molkova** 12:14 We would like to capture both?
And, you have this discriminator to… Differentiate one versus another, right?
**Minghui Zhang** 12:28 Yes, just give a choice for users, but I'm not sure if it's very important for us. For me, we just use function now.
Yeah.
**Liudmila Molkova** 12:45 I would recommend, I don't know what Alex thinks, but I… if you don't care about it, just to remove it. Somebody who cares… I have… I've never seen… Any examples around this custom thing?
**Minghui Zhang** 12:59 Yes, it's a, yeah, it's a union of, string and enam, and people could expand it easily.
**Liudmila Molkova** 13:09 Yes, I mean, you can replace it with a comment and say it's just for the future, in case other tool types will be defined.
**Minghui Zhang** 13:17 Yeah, Pat, who does that? Oh, oh, yes!
All right.
So let's, let's go ahead.
here, here is some, Mis… misunderstand, because, the parameters is, type of, JSON scammer string, right?
Maybe.
**Liudmila Molkova** 13:53 Not necessarily right.
**Minghui Zhang** 13:58 Or is it required?
**Liudmila Molkova** 14:00 Do they always have JSON schema?
**Minghui Zhang** 14:05 It's cool.
Hmm… Yes.
**Liudmila Molkova** 14:10 So I'm just suggesting a different form of what you wrote. I don't think I've changed any meaning.
**Minghui Zhang** 14:19 Yes, but, I think most of the, the definitions of parameters are, in adjacent scamma string, so, I'm trying to let the… convention more, detailed, so we can, consume the… We can consume the data more easily.
And, could you give some example, more, which are not used, JSON schema?
**Liudmila Molkova** 15:02 Yeah, so for example, the… Gemini.
Let's see, function declaration. So it actually has two different parameters. One is JSON schema, another non-JSON schema?
I don't know the details, but I would imagine that users decide to provide this.
Or that.
**Minghui Zhang** 15:32 So, so we just, don't, to… we just not to, deserialize the, JSON scam… the schema, whatever is JSON or, other scenes, we just, add them as, struct, or object, or string, to the files, right?
We don't do any, deserialization.
**Liudmila Molkova** 16:04 we… backends may, so if we say this is a JSON schema, it should be JSON schema, right?
**Minghui Zhang** 16:13 Yes.
Oh, oh, I got it.
So we just, We just left it as a vertex, what'll be… what it is?
Right?
**Liudmila Molkova** 16:34 Yeah, so today it's just whatever, right? We don't know.
It's probably JSON schema, but you see there are at least some cases where it's not, where we don't know.
**Minghui Zhang** 16:45 Yes.
Okay, I will… I will follow your, discussion… I will follow your suggestions.
**Liudmila Molkova** 16:55 Yeah.
Okay, if you would like to push for JSON schema, I mean, it would be useful to check if… which providers R… don't, don't do JSON schema. Maybe we can push for JSON schema universally.
**Minghui Zhang** 17:15 Yes.
But… but it's… it's kind of, hard for us, because, we, we just… we just, provided the… availability, we don't provide any model, model service.
For open nanometry.
**Liudmila Molkova** 17:38 Yeah, I mean, if there is some consistency, if everybody… like, it's… if it's majority that put JSON schema there, you can try pushing for JSON schema, and maybe we can say, okay, it's a JSON schema.
If you don't care, I think this… this is already an improvement to what we have.
**Minghui Zhang** 17:59 Yeah, Up to now, I don't think it's, it's, such an important scene.
**Liudmila Molkova** 18:07 Okay.
Okay.
**Minghui Zhang** 18:11 Yeah.
**Liudmila Molkova** 18:12 Cool, so then, moving on… I think what Alex is pointing to, that this, this, this is not optional. So, looking at this definition, it's not optional, but it should be optional, right?
**Minghui Zhang** 18:28 Yeah, it should be optional, I will, modified.
**Liudmila Molkova** 18:33 Okay.
Okay, so then…
**Minghui Zhang** 18:46 Yeah, I will… I would do that.
**Liudmila Molkova** 18:51 Okay.
And I had just one small comment.
**Minghui Zhang** 18:56 No more comments. Oh, yeah, sorry.
**Liudmila Molkova** 19:02 Like, the tool definition sensitive, why would somebody provide sensitive tool definition?
**Minghui Zhang** 19:10 For, for the, for the descriptions may have some sensitive, information, for my opinion, because, Mmm… People could, some people will, some people think the prompts or the descriptions might be classified And they may want to, capture some… In the tour definitions.
yeah. So, so I, I think… sorry, I think by default, we shouldn't, capture the, descriptions.
**Liudmila Molkova** 19:59 Oh, we… we don't. I don't believe we do. I think it's an opt-in attribute anyway, is it?
**Minghui Zhang** 20:06 Yeah, but, but, I mean, we should, we should, capture the type and names by default in the tool definitions, so I have modified it.
The, description in this, attributes.
You can see.
**Liudmila Molkova** 20:26 Yeah, it's not what you read there, right? It's not that you're only saying to… Put something… put part of it behind feature flag. You're saying that this contains sensitive data.
And all the variable parts, all the sensitive parts, should be in… properties, and… result if it's captured. So the values are sensitive, the definitions are not sensitive.
**Minghui Zhang** 20:59 Yeah, Maybe… maybe you are right.
But, let me see… Could… could the description of the tour's… CAP, have some, sensitive, information in it.
**Liudmila Molkova** 21:27 It shouldn't, right? It just describes what the tool does.
And what 2 does is not sensitive.
if somebody… I mean, somebody can… Put sensitive information into model name, but this is the scenario we care about.
**Minghui Zhang** 21:47 Yes, yes, Mimi, you're right. I will, Let me test it, do some discouraging, internal… internally, and, I will ask for my, For my colleagues.
**Liudmila Molkova** 22:08 Sure.
**Minghui Zhang** 22:09 Yeah, thank you.
**Liudmila Molkova** 22:10 Sounds good.
Coors.
They move on to the next peer?
**Minghui Zhang** 22:17 Yes?
**Liudmila Molkova** 22:20 Okay… So the reasoning… Yeah, I think there is just one comment to put it into the Jupyter notebook.
**Minghui Zhang** 22:43 Okay, and should I add some, example.
Right?
**Liudmila Molkova** 22:56 I think you do have an example, right? It's just, it's not… it's not in the code.
**Minghui Zhang** 23:02 Oh, yeah, sorry, I got it. I will add it. And, is, is there any scenes more, any scenes there we should, discuss it about it?
**Liudmila Molkova** 23:17 Well, my… I don't have any… I didn't leave any comments, but I was thinking that it's actually not enough, right, to define, just the reasoning part. It's a good incremental change, but we don't have… let's say we didn't capture the number of tokens for reasoning.
We didn't capture the input parameters that enable reasoning.
And, it would be useful to define them as incremental change. It does not block the SPR, though.
**Minghui Zhang** 23:51 Yes, for the, for the input and the token, I have some, I have some… I have some suggestions, As for my, research results.
I have noticed that, there are just, OpenAI… OpenAI API gives the input parameter for the reasoning, and the cloud, deep-seq, and our… our model service will not give the… inputted… parameters. Or, just to see, after now, we could, we couldn't, capture all of these, modules, input, parameters.
So, I don't think I… I'm very familiar to that… To give, commissions now.
So this ti- this task might, might be pushed, by the OpenAI folks.
But the reasoning content is important for us, so I just send this PR.
Yeah.
**Liudmila Molkova** 25:15 Yeah, and that's fine, I don't consider it blocking, I was just saying, in case you would like to contribute more, it's okay either way.
**Minghui Zhang** 25:24 Yeah.
**Liudmila Molkova** 25:29 Cool, so then this one should be easy.
**Minghui Zhang** 25:33 yes, yes, oh, sorry, I have, I have more scenes to… to talk.
The reasoning content, is, tend to be a large, a large result, more than, more than input and output, so it may be very long.
But up to now, we only have one switch, or config… configuration to, To enable or disable the capture of the, Or, or messages. So, would we add some more configuration for just the reasoning content?
**Liudmila Molkova** 26:26 If would you want to enable just the reasoning?
Like, what kind of configuration?
**Minghui Zhang** 26:32 No, no, we could just… we could enable all of the messages, and we could disable just the residding content.
**Liudmila Molkova** 26:46 I mean, we could, but essentially, we don't describe in semantic conventions.
all those configuration options, right? It's usually… more on the instrumentation side, right? We say it's opt-in, And then… It's actually difficult to deal with so much configuration, right?
Maybe we can figure out something that doesn't require configuration, some truncation strategy or something else.
**Minghui Zhang** 27:19 Yeah.
So we, we shouldn't, take, many care about the, configurations.
what… such as what, what they are defined in our semantic condition, right? We just, add some description about that, and, the implement… implementations is… depend on the… The instrumentations.
**Liudmila Molkova** 27:55 Yeah, but even in semantic conventions, like, if we say that it's a separate configuration property, we already have a few.
Can we… Do something that doesn't require extra configuration.
**Minghui Zhang** 28:18 Maybe I, I will, maybe I can give, give the… give the Spring AI, impl… implications about, this one, and, we could, we could, give, we could give more discussions, on that PR to add some, configurations.
**Liudmila Molkova** 28:44 Okay, sounds good.
**Minghui Zhang** 28:47 Okay.
**Liudmila Molkova** 28:56 Okay, so maybe we can capture the… Some thoughts here… You mentioned that Spring AI does it in some way?
**Minghui Zhang** 29:53 Yes, we have internal implementations now. I just don't, send it as a PR in the Java instrumentation, but, I will do it soon.
**Liudmila Molkova** 30:12 Okay, so, but you would like to suggest something on this PR?
**Minghui Zhang** 30:18 Yes.
Okay.
Okay.
**Liudmila Molkova** 30:38 Katie… And the last one, but not the least one… The new GenAI providers…
**Minghui Zhang** 30:50 We see the PR, at… yes.
So we just add, enam, and we will… We will add the word, or our, semantic conventions, soon, but not… not now, because it's a large work, and I will… we will need more discussion about it.
**Liudmila Molkova** 31:19 Then, what is the point of adding the constants?
**Minghui Zhang** 31:25 No, you, you could see the… I remember that you have, had some comments in this PR, in this PR, and I just replied To, to the comment.
Yes, we are planning to do that, but it's not now.
**Liudmila Molkova** 31:53 Can you add the constants at that time, then? Because we don't recommend adding constants alone.
**Minghui Zhang** 32:02 it's, it is very important, because I think, we can note… I can notice that we have, XEI, we have DeepSeek.
innate, and we… I don't notice any… Convention about Zoom.
**Liudmila Molkova** 32:23 Yeah, so we introduced this policy recently, because we, it seems everybody tries to add the constant name without actually defining things.
And we didn't change, we didn't remove, things that… We're already there, but for anything new.
We recommend adding constant along with the convention.
**Minghui Zhang** 32:52 Okay… Bad, we… we don't house so many, specific conventions about GAI. We are following open telemetry now, so most of our semantic conventions is… is the same to… The open dynamic tree.
I don't think we… we will add a… many, many.
**Liudmila Molkova** 33:22 It's still… it's the same case for everybody, right? So if you look, let's say, into… I don't know.
Azure AI Inference, OpenAI.
so you wouldn't find a lot of things that are specific to Azure AI Inference or OpenAI?
So actually, if you look into the markdown behind it, if you just follow OpenTelemetry semantic conventions, then it's trivial.
You take the span, and, and, and you…
**Minghui Zhang** 34:02 traffic.
**Liudmila Molkova** 34:03 Just extend the… extend the… this one.
And it's just a few extra things you do in YAML.
**Minghui Zhang** 34:15 Yeah, I, I got, I got it, But, it's kind of, a replica of the… or doing AI span… Fires.
Right?
**Liudmila Molkova** 34:33 Yes, so… If there is any flavor you would like to add, you add this flavor here.
Right?
And, it's trivial, it gives you the place where you can document things, and then maybe some attributes are not applicable to your case, and then you remove them. Maybe some of them are Populated in a special way.
**Minghui Zhang** 35:02 Yeah.
**Liudmila Molkova** 35:03 So, it should be trivial, you don't need to have a lot, it is just… helpful to have a dedicated place for your conventions, and you're confirming That you are not deviating from semantic conventions.
By just repeating things.
**Minghui Zhang** 35:24 Yes, yes, it makes sense. I would do that. Thank you.
**Liudmila Molkova** 35:29 Awesome, thank you.
Cool, so it sounds like we are… we discussed all the pull requests.
Great work!
**Minghui Zhang** 35:46 Yes, thank you. So, T?
Sorry.
Okay.
So, Archie right? Do you have any, some things to.
**patrickpok** 36:10 Not for today. Today was really for me, like, to get to know you a little bit. It's, again, like, I'm really coming from the Java side, but much more, like, with the servers, and now we are with the AI thingy, like everyone else, so I was just wondering what you guys are doing. It's very interesting, but nothing from my side anymore.
**Minghui Zhang** 36:29 Yeah, thank you.
we, I'm now, trying to, trying my best to, implement, the Java side, instrumentations, and maybe we have, we could have more, connections.
**patrickpok** 36:48 Yes, definitely.
**Liudmila Molkova** 36:53 Cool, so then thank you both for coming. We will have another call tomorrow, well, tomorrow for me, today for maybe both of you.
And there are… we… This call happens every two weeks, well, if you're lucky. And the other call happens every week.
So if there is anything else you would like to discuss there, Minghui, please, I don't know, bring back your PRs, we will make sure to look at them.
At tomorrow's call.
**Minghui Zhang** 37:29 Okay, I don't think we have more, more scenes to… to talk.
these things, if the blogs are, con… interested in this, PR, you can just, discuss about it, but I will… I couldn't, attend the… for me.
I'm more wrong.
**Liudmila Molkova** 37:56 Yeah, of course, of course you can't, I mean, you can just put the… Next section here, if you want us to pay attention to anything in particular.
**Minghui Zhang** 38:10 Yeah.
Of course.
**Liudmila Molkova** 38:14 Then, thank you both. Have a great rest of your day.
**Minghui Zhang** 38:19 Goodbye.
**patrickpok** 38:21 Have a good evening. Bye-bye.
**Liudmila Molkova** 38:23 Thanks, bye.
