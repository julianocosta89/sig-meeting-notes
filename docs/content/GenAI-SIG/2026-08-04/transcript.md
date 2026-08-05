SIG: GenAI SIG
Date: 2026-08-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker (Microsoft Corporation) 00:01:52 I'm a little worried people are in the old… maybe the old Zoom link.
So, I'm going to… see if I can find that old Zoom link and join over there.
But I'll be back.
Habiba Mohamed 00:02:14 Do you think it's… is it on the Word doc, or… Where's the old Zoom link?
Trask Stalnaker (Microsoft Corporation) 00:02:19 The… it got copied… it was on the old… I'm going back in time in the Google Calendar.
Habiba Mohamed 00:02:31 I see. Were you saying you were going to tell people to join here, or we should all.
Trask Stalnaker (Microsoft Corporation) 00:02:34 Yeah. No, no, this… I think this is the correct one now.
Habiba Mohamed 00:02:38 So it was just the… okay.
Trask Stalnaker (Microsoft Corporation) 00:02:39 Stay here, yeah.
I'll be back.
Mohnish 00:02:45 Hey, everyone.
Good morning.
Oh.
Is it morning for you all, or are you all based out of the US, or…
Habiba Mohamed 00:02:57 Yeah, it's 9 AM for me.
I'm… Based out of Seattle, so… Pacific time. Yeah. Morning.
Mohnish 00:03:05 It's 10 for me, I'm from, Boulder, Colorado.
Habiba Mohamed 00:03:09 Mmm, so Mountain Time, okay.
John Mcbride 00:03:12 I used to live, out in Denver. How's the weather out there?
Mohnish 00:03:15 Oh, that's awesome. It was hot, the last week, so it was 101 or 102, but today it's a little cold, so yeah. I'm a student from CU, so…
John Mcbride 00:03:27 Nice.
Mohnish 00:03:28 Yeah.
Habiba Mohamed 00:03:29 I'm going to Colorado next week, since we're talking about Colorado.
Mohnish 00:03:32 Oh, that's awesome.
Are you up to Denver, or anywhere else?
Habiba Mohamed 00:03:36 Aurora? Oh, that's y'all have heard of it, a little south.
Mohnish 00:03:39 Yeah.
Habiba Mohamed 00:03:40 Actually, I don't know where it is relative to Colorado. I'm assuming south, but…
Mohnish 00:03:44 Right, yeah, it's a little, like a 30 minutes drive from Boulder, so…
Liudmila Molkova 00:03:52 Hello!
Aaron Abbott 00:03:53 Good.
Liudmila Molkova 00:03:53 Sorry for being late.
No, a couple of us were in the…
Aaron Abbott 00:03:58 Sorry, a couple of us were in the other meeting room, so I just put a link in the, Meeting notes, I think it just took the… the change with the new Zoom link.
Liudmila Molkova 00:04:08 Go ahead.
Trask Stalnaker 00:04:09 Oh, do we still have the old Zoom link in the meeting notes?
Liudmila Molkova 00:04:19 No, it's the new one, right? The LFX.
Trask Stalnaker 00:04:23 Okay, good. Yeah, yeah, Aaron, I must have missed you, because I just hopped over there to, because I was like, nobody's in this meeting! Where is everybody?
Aaron Abbott 00:04:35 Yeah, I had a still copy on my calendar.
Liudmila Molkova 00:04:43 Bye.
So let's get started. Please add your name to the attendees list, and if you want to discuss something in particular.
Please add your… Items to the agenda.
John, you posted, yes, Why did it move to a LFX platform? I think it's a CNCF requirement, maybe Trask could no more.
Trask Stalnaker 00:05:17 Yeah, they're, canceling our Zoom, accounts, and, that we had, and moving through… Now we have to use this, It's supposed to be better. Is there, what is the… Issue that you're running into.
John Mcbride 00:05:40 It's… you can't actually join the Zoom anonymously. It forces you to put… name, information, organization you're associated to are actually signed into the LFX platform. Which, you know, I know a bunch of them, so I'm happy to go provide that feedback to them upstream, but it was, it was a bit, It's a bit jarring if you're, like, somebody who… you know, maybe doesn't want to advertise that you're working at Google, or advertise that you're working at a startup, or don't want to tell the Linux Foundation that you are a startup working in this ecosystem or something, right? Many reasons you might want to join anonymously.
Liudmila Molkova 00:06:16 I think you can still… you can… you don't have to provide your company information. Somehow I'm here without my company information appearing, and worst case, you can say independent, and… Use a fake name. Well, please don't, but yeah.
John Mcbride 00:06:35 We can, it's a dark pattern. I don't know, we don't have to get into it, I can provide that feedback to them.
Liudmila Molkova 00:06:41 Yeah, thank you, appreciated.
Trask Stalnaker 00:06:43 Cool, and we won't kick you out if you join under a fake name.
Liudmila Molkova 00:06:48 your GitHub alias.
Trask Stalnaker 00:06:50 Yeah, yeah.
Liudmila Molkova 00:06:55 Awesome. So, we usually have packed agenda, and, let's just start with the… Items we have Trask, you wanna talk about tool description and definition?
Trask Stalnaker 00:07:09 Yeah, so… I got this request, to mark these two attributes as sensitive.
And the… kind of digging into the reason, because at first it didn't quite match up, to my thinking.
But, the use case is when you're creating the, creating a tool, like, dynamically in code, and… You want to give the agent, sort of, the best possible chance of using it, and using it correctly, you may want to put in Detailed information. For example, a username.
Even into the description, saying that, you know, hey, go and, you know, check the… here's a tool to check the account balance for this person specifically.
And… So… Information can leak in that way.
The… tool definition, is opt-in already, and is large, and, like, I… I think that one is the… that's the easiest sell for me.
The worry I have about marking the description as sensitive is that… Do we… well, I guess we do probably have some recommended attributes in HTTP that can contain sensitive info? I forget.
Liudmila Molkova 00:09:06 the URL?
Trask Stalnaker 00:09:09 Yeah.
Yeah, absolutely. Okay, so I take back my reservation about that one.
But wanted to see what other people thought, thought, any feedback on that before I… open a PR since, was, at least initially, was… I was not… Sure about it.
Liudmila Molkova 00:09:34 What do we do today?
Trask Stalnaker 00:09:37 We don't say anything about it being sensitive, either of them.
Liudmila Molkova 00:09:42 Oh… Okay, so this is sucked in, and you want to make it sensitive, and… Oh, description… oh, it's recommended.
And you want to put the sensitive markers inside them.
Both.
Trask Stalnaker 00:10:00 Yeah, yeah, I don't think it shows up here, but it would show up in the footnote.
Liudmila Molkova 00:10:04 Huh.
Yeah.
Okay, yeah, we can do this better, like, with the annotation and YAML, but let's ignore it.
Trask Stalnaker 00:10:15 Oh, yeah. Yeah, yeah.
Liudmila Molkova 00:10:20 Okay, sounds good to me.
Trask Stalnaker 00:10:27 Cool. If no other… Comments? That's all I… wanted to get an initial feeling. Certainly, feel free to object on the PR. I just wanted to read the room first.
Liudmila Molkova 00:10:44 Yeah.
Thank you.
Habiba, the guardrail. Do you want to present?
Habiba Mohamed 00:10:58 It looks like my headset mute, unmute function's not working, sorry about that.
Trask Stalnaker 00:11:01 We got you now.
Habiba Mohamed 00:11:02 Yeah, you got me, okay. So yeah, I'm taking over the PR from Nakumar. So I've made a lot of the updates from PR262, I've made a new fork, created a new PR, And then I addressed… so I'm addressing the comments in the old PR just to track it as I make the changes in the new PR. I did want to bring up just one thing, at least for now, was the, Sorry, how do you pronounce your name? I want to make sure I pronounce it correctly. Was it Lududmila?
Liudmila Molkova 00:11:33 Yeah, Liudmila, pretty good.
Habiba Mohamed 00:11:34 Okay. Yeah, so the… there was a comment about collapsing for namespacing, I think it was… where's my point right there? The, so GenAI security guardrail versus GenAI guardrail, and I wanted to discuss that as a group, because I think with guardrails, there's responsible AI. It's not all always security-based, I would argue, and so I know it's getting pretty long. A lot of the, like, additional sort of things that we're adding to it, what's everyone's thoughts on EdRad? That's the only thing I wanted to… the next item I was kind of going through.
In the PR.
like, GenAIG guardrail versus GenAI.security.guardrail.
I would like to keep security guardrail, like GenAI security guardrail.
The reason why is that guardrails can come up for various reasons, not just security. So, I would imagine in, like, in instances with responsible AI, if you're applying policies, I wouldn't say it's exactly, like, a security scenario.
Liudmila Molkova 00:12:48 that that's a good reason to not put it in the security namespace, or… Or, like, would it…
Habiba Mohamed 00:12:53 come after, then… okay, that makes sense. Okay, so I guess my question was, like, if we were to put, for example, GenAI guardrail, and then we were doing some attributes, like, some outputs from, like, classifiers or something like that, like XPIA, like prompt injection, then I feel like it would kind of… I guess it's… okay, so then I guess that is a reason to kind of… it is just a generalized guardrail for anything. Okay, sounds good. Kind of just rubber duck that. Okay.
Liudmila Molkova 00:13:22 I don't… yeah, I don't really know the right answer, but, like, something like word rail names seems pretty generic.
the guard…
Habiba Mohamed 00:13:31 Yeah.
Liudmila Molkova 00:13:32 Well, this is not a guardrail anymore.
Habiba Mohamed 00:13:37 I guess there… I guess there are instances where you could have a non-security action, a non-security verdict. So maybe the idea is that maybe we do GenAI at guardrail.security after for at least the spans that are related to security actions, or recording security events.
I guess I just don't want to lose the security aspect.
Of it.
Which I think it's, it's useful.
Trask Stalnaker 00:14:06 In the reference instrumentations, I'm wondering, how do you know that a guardrail is security-related or not?
Habiba Mohamed 00:14:17 So a lot of the times, it just… it's the name is the description of it, so there's not really a standard way. Usually, it's the description of the name, so… Which is why I think it would be useful to actually have.
the, like, denotion, so we know it's a security guardrail versus just a policy guardrail. But Ankit, were you gonna say something?
Ankit Singhal 00:14:39 So, for non-security guardrails, like, is a suggestion to do something like GenAI.Guardrails.
Whatever specific that got released, or it could be, like, policies within an organization, or something else, right?
Is that the suggestion as well, for the non-security guardrail?
Habiba Mohamed 00:14:57 Oh, I see. So, like, to put GenAI guardrailtype dot guardrail, so it's GenAI policy guardrail, security guardrail, yeah, that's the…
Ankit Singhal 00:15:09 I could go either way, to be honest, but just, like, since we are making that distinction of whether it's a security versus non-security, and it could be more categories, like, going forward, right, for policies that you apply, and… So…
Habiba Mohamed 00:15:22 That makes sense.
Liudmila Molkova 00:15:25 Currently, there is just a name of the guardrail, that's the only property, and it's super generic.
Habiba Mohamed 00:15:31 Yeah, which is why I think because there was the security, like… before guardrail, it made sense that it was a security guardrail type, and so then the name would be like, okay, this is the name of a security guardrail. I feel like we would lose that if we got rid of security.
I don't know, I guess I'll look into maybe… I'm not sure if guardrails can, like, I don't know if we're gonna get some sort of, namespace clashing, or just names of guardrails that could be similar for a guardrail that's for security purposes versus policy.
But yeah, we can take… we can continue more in the… in the PR, right?
Trask Stalnaker 00:16:09 Yeah, I'm wondering how… I'm so curious how instrumentation would know whether the guardrail was security-related or not.
Habiba Mohamed 00:16:21 Yeah, it wouldn't, so that's why I think we need… we would need that, sort of, like, GenAI, or at least something the span name.
to denote that it's a security guardrail. Is that what you're asking?
Trask Stalnaker 00:16:31 But if… well, no, if instrumentation can't tell… then how do we even populate it? How do we even populate that it is security?
Habiba Mohamed 00:16:45 Oh, I see, okay. So I thought it would be up to whoever's doing the instrumentation, right, to be able to… when they, like, when they set that span, right? Is that what you're referring to, then, or…
Trask Stalnaker 00:16:57 Well, so there's… there's entirely manual instrumentation, right? Where you're writing, you know, you're writing everything, and you're building your own spans, and so you can populate whatever you want on there.
But most of the instrumentation that people use is instrumenting frameworks.
So, would be a generic instrumentation for a guardrails framework.
And something that could automatically, you know, create those spans, and that wouldn't know if it was security-related or not.
Habiba Mohamed 00:17:39 I see, I see, okay, that makes sense.
Trask Stalnaker 00:17:41 There may be ways for us to… address that? Like, especially now with context Scoped attributes coming, where users could… Say that, you know, this is… Security something, and they could provide Additional attributes that would get automatically stamped onto the automatically collected spans?
And we can always explore, like.
Kind of bespoke manual instrumentation things, but generally where we like to start here with semantic conventions is… What are things that we can… that frameworks can natively instrument and capture.
Habiba Mohamed 00:18:34 That makes sense. Okay.
Liudmila Molkova 00:18:39 And for this, does OpenAI have a notion of guardrails or OpenAI agents?
Habiba Mohamed 00:18:47 I… I… okay, so there was a couple of references. I haven't gone through the actual, libraries that, Nakamura had linked, but I believe there was… a lot of it was referencing OpenAI, so… Yep, okay.
Ankit Singhal 00:19:04 We can… yeah.
Habiba Mohamed 00:19:05 Perfect.
Surya?
Surya Teja 00:19:10 Yeah, I was actually, there is, guardrails from OpenAI, as well as Microsoft has some… got some rich, APIs and SDKs for, this thing.
Are we also… In engaging them in this, instrumentation?
Habiba Mohamed 00:19:34 Sorry, what is this thing?
Surya Teja 00:19:35 In the instrumentation that we are having, Microsoft also has some, guardrails kind of, APIs and, stuff.
Are those also part of these, this instrumentation?
Ankit Singhal 00:19:50 Yeah, if I'm not sure, Habiba is from the RAI team from Microsoft, from the same team that you're talking about.
Surya Teja 00:19:56 Okay.
Ankit Singhal 00:19:57 Yeah.
Surya Teja 00:19:59 And, is it also… are we also go targeting the OWASP, 10 threats or everything with this kind of data?
Habiba Mohamed 00:20:06 integrated, the OWASP will be up top 10 for LLMs, yeah.
Surya Teja 00:20:11 Okay, okay. And also, the third, last question, is there was a… Issue from someone.
who was a maintainer for one of the… I don't know what kind of repo that is. They asked… they created something, and they left a prototype.
And I asked him to look into it, and he said that there are some differences. I can throw in the issue link. Can we see if that can be… Included in this one, or is it something different than what we have planned for this one?
Habiba Mohamed 00:20:45 Why don't you… why don't you throw the link in? I'll look into it and see if it's relevant. Thank you, yeah.
That's what I had for that. And then, oh, also, one more question. I think this is for Aaron. I don't… so Nakumar had left a comment on the PR that… that you were collecting some feedback from the model armor team. I'm not sure if that feedback's been integrated. I believe it was, but we can clarify that offline as well.
Aaron Abbott 00:21:12 Yeah, no, it should be there, so if you go back to the original PR, And then if you… I don't know if there's a way to see the approvals from this page, but if you go to, like, the main tab.
Habiba Mohamed 00:21:25 Yeah, I think it was, like, a top-level comment.
Aaron Abbott 00:21:28 Yeah, even just the approval, so, Himanshu and Shubim?
Habiba Mohamed 00:21:32 Oh, I see, okay.
Aaron Abbott 00:21:33 We're… are from the Model Armor team, so they… they left an approval. I'm happy to get another… get them to take another look at the new PR, but I think the feedback was already incorporated.
Habiba Mohamed 00:21:43 Okay, sounds good. Alright, thank you all.
Aaron Abbott 00:21:46 Thank you.
Liudmila Molkova 00:21:48 Thanks. I have a question to you both, Habiba and Erin.
The things we are introducing here seems to be exhaustive.
Or it may be in the old PR, I didn't see the new one yet.
Do we know we need it all? Or do we, like, assume that this would be useful?
Can we separate one from another?
Habiba Mohamed 00:22:12 So there were a couple of properties I removed. I think there was one note you had left about… I think it was, like, evidence, or some sort of evidence string, which I said we should remove, because you can't sort of redact that. It could have customer content, and it shouldn't be in… In the telemetry, but I'll look into it, but from what I see, like, we need all of it, because a lot of it will describe exactly what happens in the event of, like, a security.
Even… but I'll review the fields just to do another look. So, so far, I've ported over just everything Nakumar had in his PR, but I'll look again.
Aaron Abbott 00:22:50 I'll also take another look.
Trask Stalnaker 00:22:54 One question I have is sort of, still a, back to the kind of generic guardrails versus security guardrails.
Just to think about… I don't… I don't know the answer here, but, if it would make sense to define generic… kind of just the basic guardrail structure.
Spans, basic attributes, and then, sort of.
We could layer security-specific guardrails on top of that.
if that helps us to think about them and maybe break up the PR… Really not sure.
Habiba Mohamed 00:23:36 Yeah, I think that's what we were trending towards. And then also thinking about this on the flip end, like, once you have logs, being able to run, like, large-scale detections as well would be useful the more specific the guardrails are, and what you essentially have in the logs.
Because a lot of it then will end up having these sort of data pipelines where we have to then label, the logs and sift through them, so the more, sort of, like.
you know.
Very much, more specific, the better it'll be for detections on the flip end as well, in case of a security incident.
Liudmila Molkova 00:24:15 Nope.
Habiba Mohamed 00:24:16 Yeah, thank you.
Liudmila Molkova 00:24:16 Looks like, like, if you look here.
We probably should at least have common properties, and this is a generic guardrail, right?
And we know it's an output guardrail because of the type, And if I look… Here, I think the… We have the name, Which should probably be this function name.
Right? But the fact that it's targeted at output I think it's currently recorded, let's say, on the… The third… the security namespace.
But in the case of, like, a generic guardrail, it's actually a property of the guardrail itself.
So maybe it would be a good exercise to, like, Compare it against this.
And we even start with this, because it's… Instrumentable by default.
Habiba Mohamed 00:25:27 Makes sense, yeah.
Liudmila Molkova 00:25:30 Thank you.
Habiba Mohamed 00:25:32 Alright, thank you all.
Liudmila Molkova 00:25:37 Okay.
So, should we move on to the Ankit topic, the real time?
Anthu, do you want to present?
Ankit Singhal 00:25:51 Yes, please. Thank you, appreciate it.
Liudmila Molkova 00:25:53 Sure.
Ankit Singhal 00:26:04 Okay.
Thank you for the feedback. I saw a couple of comments, and I think I wanted to, address, like, one of the major ones, which was around whether we should use the chat span, which is the inference span, or should we have a new span for real time? So… For that purpose, I think, that question is a very good question. I don't think there was a simple, straightforward answer to that, so that's why I put down this talk, to kind of get more data and help us make that decision together. So… I want to go over, like, the differences between the influence and the real-time.
voice models, and from there, we can go on, like, how they differ and how they are similar, and we can make a decision on that. So, first was around the transport. So, for the chat or the inference panel, there's one request, one response, and that's it, right? And then it's that. For real time, it's a long-lived, bi-directional session. I know here it's written WebSocket, but there are WebRTC as well that's there, but it's a long-lived bi-directional session.
And then, second is about the statefulness. For the chat and inference plan, there's… it's straightless. However, you can pass in the conversation history from Previous runs, like, in response API, you can save previous response ID, or you can have the entire chat history passed in, so things like those, but it's still stateless.
For the real time, it's a… It's stateful, where, like, the model or the… as a part of the connection, the conversation history is, somehow managed. So, and when, When multiple turns happen.
Oh yeah, was there a question there?
Yeah, okay. So, when there are multiple turns, like, for, subsequent turns, the previous turns, context is maintained, and during that session, model knows about that.
And for the streaming, real-time is always streaming. Chat inference, it's optional, you can do streaming versus non-streaming.
And then in the chat inference, the turn boundary is explicit, where a client sends a request, you get a response, and then your turn ends, right? In the real time, there is a concept of turns, but you have to look into, how that's configured using voice activity detection, VAD.
And customer can control that when they are doing the session creation, so that's another big difference between these two.
For the outputs, I think, there, to be honest, there's not much difference between chat and real-time, because now, even, through chat completion, the responses API, you can generate… you can give audio as input, audio, and it can generate audio as output. I think the only difference that I came across was For the input audio, for the real time, there is a way you can get the transcript of those as well.
Which is not present for the, charge and transform.
And for the chat inference, for every call, you can pass in parameters and you can modify those. However, in real time, depending upon the providers, there are only a certain set of parameters that you can change during a turn, whereas most of them are configured during the session creation.
And they apply to your entire session.
And then, like, for the chat inference, like, multimodal inputs are possible, and for the real-time, it's more like speech-to-speech right now. So, on a high level, like, these are, like, some of the conceptual comparison that I wanted to do to kind of help us understand.
And then, audio modality, I think right now, like, the chat functions that we have in GenAI spec does not cover the audio modality that well, but I think that something is supported in that location right now.
And I think that would also apply to real-time in a way, about, like, how do you, like, either if you have a… Input and output, which is an audio.
How do you model that, right? And things like those.
Okay.
So… so that's, like, in a high-level comparison for these two. And the other one that I wanted to talk about was the span boundary, and one of the decisions that's made in this, or that's being presented in this PR is.
Whether we have a span for the session, or whether we have a span for the turn, or both, right? So, I think this PR suggests we should have a span at a turn level, not at a session level.
And one of the major, reasons for that is, like, these… connections or the sessions, in case of the real-time voice model, can be hours long. And OpenAI has a limit of, right now, 60 minutes, but these can be, like, really long-lived sessions if we model them as sessions.
responsive.
So, that's one other thing, and then the other thing is, like, you can obviously, like, correlate the spans using some sort of session identifier or conversation identifier.
Here, please go ahead.
Yes, Johanna.
Aaron Abbott 00:31:14 Is it alright if I ask a question, or…
Ankit Singhal 00:31:16 Yeah, yeah, yeah. Actually, that's good, yeah. I think that'll help us clarify.
Aaron Abbott 00:31:21 Yeah, so I think I was chatting with Ludmila about this too, but how do we identify a turn in the, like, real-time conversations?
Ankit Singhal 00:31:29 Yeah, yeah, okay. So I think I have a section for the VRE, which kind of, talks a little more about, like, there is turn identification, and it… based on the configuration, it can be done, like, whether you can totally disable it, and then there are some cases where a long pause can be a turn reduction, where server actually assumes that, okay, if there is a… based on the configuration, if there is a delay. So, those kind of configurations are available, and once, you know.
That's when, like, your model will start responding.
or we'll assume that your, like, customer has, or the user has stopped speaking, and it ended. So, there are ways to know, like, the turn has ended.
Aaron Abbott 00:32:13 Okay. Are those, like, semantics that we would enforce, or is it part of the data model of the real-time APIs already?
Ankit Singhal 00:32:20 Yeah, it's there as a part of the… already the real-time APS, both Gemini and OpenAI real-time model server.
Aaron Abbott 00:32:29 Okay. Like, I know…
Ankit Singhal 00:32:30 They're pretty similar, semantically, but the parameter names are different, but that's…
Aaron Abbott 00:32:37 Yeah, I mean, I can take a look offline as well, but, like, just for my,
Ankit Singhal 00:32:42 Yeah.
Aaron Abbott 00:32:43 For me, do you mind explaining? Yeah.
Ankit Singhal 00:32:45 Oh, yeah. Like, is it margin?
Aaron Abbott 00:32:47 Or is it something else that you see in the event stream that you know, Yeah, yeah.
Ankit Singhal 00:32:53 Yeah, I think there are multiple of the different events. Like, one is, like, interruption.
And then there are, like, automatic These are more like, I think, the config file. I can check on if I've put in the exact events for those. If not, I can put those, but I think there are.
And… If there are more questions around that, definitely I can… Kind of.
Put together some samples, if that helps.
Liudmila Molkova 00:33:26 Yeah, I have some questions. I'm interested in this from the… Google Gemini Life, agents, and I've been researching it and the difference between these two.
I kinda have a couple of… things, really, that I want to discuss about turns and about the span boundaries.
But, do you… do you want to… Talk about anything else, where you would, like to take it, concern by concern?
Ankit Singhal 00:33:58 Yeah, so I think, definitely, like, I would definitely love to talk more about that, both these parts, like the span boundary and the turn detection, right? The other one that I wanted to also present a few things around, like, whether we can reuse the chat inference span, or we need a new span. Like, there's some data I've put together to kind of understand How much of those attributes which exist are applicable to real-time versus what are new.
And whether, and that can help us make that decision.
Yeah, I have that part as well, so I can go in any order, that works for me.
Liudmila Molkova 00:34:37 So maybe we can do this. I… I have some doc I also posted in the… Our meeting not,
Ankit Singhal 00:34:46 Yeah, I just thought I'd just want to share.
Liudmila Molkova 00:34:48 Yeah, yeah, of course, yeah, I just finished it this morning. Maybe I'll quickly go through my findings, and then we can talk About this together.
Ankit Singhal 00:35:00 Got it, okay. And, I just wanted to mention, I think I tried to separate the voice model inference versus the voice agents, right? Because I think my initial PR works for voice agents, but then we had this feedback about, like, can we separate or make it into smaller PRs? So, this is mostly focusing on just the Voice model inference, by the way, yeah.
Liudmila Molkova 00:35:21 Yeah, yeah, hopefully.
Ankit Singhal 00:35:23 Yeah, please, Clint.
Liudmila Molkova 00:35:26 K, so, I… One sec… So, I was trying to approach it maybe from similar angles, but slightly… Different, and… Somebody internally pointed out that, Langsme has just released their tracing story for… voice agents, and… inference, and… Well, it's an interesting document. They record essentially every event.
Has this been?
The main argument that like… As a user, when I speak, and I can interrupt agent, than… Our turns, like, the turns that, we take are… just random. Like, we don't really clearly know on the client when the turn starts, when the turn ends.
I think they would be right if turns could, like, intersect? Inter, if… There… if the… like, if the model Would keep listening to you.
and… as it speaks, it would also take into account what you talk, but while keeping the previous response open. But I think it's not the case, the turns are kind of interleafed, they don't intersect, so then I think their idea that events are absolutely necessary, and we cannot represent turns as spends, or that they don't have duration, is kind of not applicable. Hey, Trask are muted?
Trask Stalnaker 00:37:21 Even if they did overlap, why would… why would that mean we shouldn't use fans?
Liudmila Molkova 00:37:30 Because we would not be able to know, to correlate information to a certain turn, I would guess.
Trask Stalnaker 00:37:40 Okay, that was the part that I wasn't sure about. Like, I was assuming that there still was a request response.
Like, you say something, and it's responding to what you said, and… You might have interrupted it sooner, and that might overlap.
But there's still… the question to me is whether there's correlation between the response coming back on the WebSocket and the request.
Like, does it pass back a request ID?
Ankit Singhal 00:38:13 So, there is definitely, like, a response ID, you know? Like, once you send in a request to a GPT real-time model, you get back, like, it's gonna stream… you can stream, like, there are multiple events that's gonna be done. Once the response is done, or as a part of that, also, you can get the response ID, and that tells you that, okay, now this response is done.
And then, about the, I think one of the interesting part about the voice agency is the barge-in or the interruption.
And… as per my understanding, as per my research so far, like, I've looked at multiple of them, like, most of the providers support where if the response gets interrupted, like, when the model is producing a response, if it gets interrupted by, like, a human speaking.
then it ends that response there, right, and then starts a new one, based on, like, what the user is saying. So there definitely is, I do, like, probably, like, that's my understanding, and based on that, there's no kind of real overlap between… yes, like, as, as the agent, or not the agent, the model was, like, giving the response, yes, it got interrupted, but it then ends the response, and then… And the part that it actually told you already, like, which is not the full part, you can still transcribe them, and then be made available as a part of your output, to kind of see, okay, this is where it happened, right? And you can capture that interruption, too. So… Yeah.
Liudmila Molkova 00:39:34 And I agree that the length Lexis maybe overdid it, or maybe they are trying to target some other cases where they want to know the precise timestamp and users stopped listening, and this is kind of hard to do because the content understanding happens on the model site. But I… I kind of used this research to… and came up with slightly different conclusions. So, I think the… the… from what I see in OpenAI, they… have a notion of request-response, but it's the same as an inference. So, like, if I… if I can show you this picture, this is me playing… this is a picture of a Google thing, but, this probably demonstrates what, and Ankit here talking about. So, for this front.
this is what OpenAI has with request responses. They're… Usage of inference looks pretty much the same as… For inference, except… And I think maybe Ankit could disagree with me, but… The thing that we know is not when request has started.
We know when response has started, when the response was created, not when the request was made. When the response was created, because we receive an event from the server. And then we know when the response has ended.
And this marks the individual inference span, so if you have a tool call in the middle.
Then, similarly to inference, this tool called Would, like, interrupt one inference, you would send the results back, and then you would be able to track another response.
So these two friends are actually what you see from the OpenAI events.
Ankit Singhal 00:41:36 Yeah, and this is similar to… And this is similar to how, like, the text model works, right? Where model decides, okay, I'm… like, this is for an agent, right? So, an agent decides, okay, I need to call this model, right? To make sure, like, if I need to call any tools, or… and that… that agent, or, like, for example, like, the Generate Content Gemini in Live 1, right, so… And logos to in the… Data models, would be, or text models would be.
chat span, and there, that LLM tells you, okay, for this request, you have to make a tool call, and then a tool call is made, right? And then it gets a response from the tool, and then gives you a final response, right?
Same kind of behavior here so, right?
Liudmila Molkova 00:42:20 Yeah, so I think it's almost okay for OpenAI to pretend it's just a regular inference span. Whether it's a good idea or not, I don't know, but I don't think there is, like, any strong deviation.
For… Gemini, it's a little bit more fun, because Gemini doesn't… really… operate… At least from the outer level, the Agent side, it doesn't… operate on the request or, like, inference level. It talks about turns. The turn is the… Actual step, there is a turn complete.
The terrible part about it, that for… For OpenAI, you would get usage on this, friends.
So this Friends are actually in France.
for the Gemini, they don't… like, I can't fake them. They are totally faked.
I don't know the start time.
What I know is the outer thing, it turned.
And it contains usage, and I can almost guess its duration.
Almost reliably.
But, like, it sounds like the Gemini works in one layer.
And OpenAI works in a different layer, and I still don't know how to reconcile, like, how to model them, how to model some generic thing that would apply to both.
Because… Impossible.
Ankit Singhal 00:44:02 Maybe, maybe I didn't understand the, Gemini Life part, like, how it's different, maybe I can reach out to you more on… or more questions on that, because, like, the sample that I had for the scenario for the Gemini, like, to me, it looked very, very similar to OpenAI GPT Real-Time, but in case I'm missing something, I would definitely love to understand that point.
Liudmila Molkova 00:44:28 probably need to look more into your example, but I would love if you could read this doc, because I have these events here.
And the… the comparison… So… What's interesting is that this response is per inference thing.
And… So there is some signs of it in Gemini. This is the events I'm actually getting from the model.
and… This talks about generation complete, it never talks about generation started, and then there is a turn complete.
Well, it never talks about turn being started.
I think we're deep in the weeds. One thing I probably have a strong opinion on is that this, a model that does invoke Agent It… it… I… I don't know if it's an invoke agent. I… I would… I don't think it's an invoke agent. It's the turn, right?
But for OpenAI, if I understand correctly.
It's totally fake. It's like you're… you're… Detecting the start of the turn.
As the start of the first response, and you detect the end of the turn.
When the finish risen is stopped.
Like, how do you know what happens if there is a tool in between? How do you know about turns.
Ankit Singhal 00:45:58 I mean, when the response completes, that's where the turn ends, right? It could be the response completed from the model, or there was an interruption It could be either, but it doesn't.
Liudmila Molkova 00:46:10 But this is, like, if you have a tool pole in the middle, this would be two different turns for you, no?
Ankit Singhal 00:46:16 Oh, so actually, I'm just talking about the inference part, like, which would be similar to, like, in chat, like, you have a finish reason, right?
But in Work Agent, yes, right now, nothing exists which can tell you if it's just in Work Agent operation.
like, ended because of margin interruption or something else, I think that's something… like, at least the PR that I was referring to does not cover, because that's more of the… modeling of the voice agents. I mean, this was just more for modeling of the inference part alone.
Liudmila Molkova 00:46:49 Okay, and then maybe this is where the difference is, because…
Ankit Singhal 00:46:55 And for voice agents, we'll probably have to look at much, more… there are a few more providers.
And I've listed them in my… the original PR, which I think will help us understand a bit more on, like.
Like, VAD detection, turn detection, because there is definitely, like, a way to kind of detect that turn.
And if there are more details on, like, what's missing, we can definitely, dig more into those details.
Liudmila Molkova 00:47:27 Okay, I… I… my observations are different. I don't think it's… it's obvious how to detect its own, but yeah, we can look into this.
Additionally, what I'm saying probably here, if we limit ourselves to inference, that I would not be… I would not feel comfortable saying that I cannot… I can have… I can actually produce the spans for life.
For Google. And this one, for example, it doesn't… the span… Starts… at random point, I just don't know when it should start. I don't have any events saying when the content starts, like, when the inference starts.
Ankit Singhal 00:48:07 I see. So, actually, for that, I had a sample, so maybe if you feel like there is not enough information in that scenario.py for Gemini Live, then I think I would definitely want to work on that and make sure it's up to the expectation there.
Trask Stalnaker 00:48:26 That's what I was gonna ask, Ankit, is whether you had the reference scenarios, or…
Ankit Singhal 00:48:32 Yeah, it's there, like, for a Gemini life, we go down to… Scenario.py under Gemini Ledge.
Liudmila Molkova 00:48:42 But you, you, you, you have run in French, right?
Ankit Singhal 00:48:46 Yeah, I think that's just, like, a logical kind of, Method to show where we're actually calling a model.
So, line… 74, I think that's where I think this reference implementation creates that inference plan.
And then…
Liudmila Molkova 00:49:09 Yeah, so what, like, happens is that you call this, and it's a continuous stream, right? It never ends.
Ankit Singhal 00:49:17 It does end, right? It does end.
Liudmila Molkova 00:49:21 Well, because you ended.
Ankit Singhal 00:49:23 They may be.
Liudmila Molkova 00:49:23 Okay, in reality, you… Just keep talking.
and the model detects, like, you… I can start a chat, And… Just keep silence. At some point, they will start talking.
The stream is sent to the model.
Western Gemini case, and models decides, okay, actually, you said something, finally, and you actually stop talking, and then it sends an event.
Saying, okay, I detected that you've talked.
And then… It's the model which drives the… When inference happens, you're lucky if you know that it happened in OpenAI, and Gemini doesn't tell you.
Ankit Singhal 00:50:18 Okay.
In Gemini? Oh, no, sorry, more like that.
There it is.
Liudmila Molkova 00:50:32 And even here, it just happens that you write the span before you start session receive.
In rail instrumentation, you would need to detect the first Like, you would start the spam when you receive the first.
Event from the session.
Like, when somebody calls, the session receive.
Which is effectively the session spend, not the… the turns pen.
Ankit Singhal 00:51:02 So you're looking for something which can help us identify that the influence has started from the model side, and it sends… and it lets you know by some sort of event, right?
Liudmila Molkova 00:51:12 I'm saying, like, when we instrument this SDK.
We need to instrument it without… knowing when things start. Here, you know when things start.
Like, I think the reference scenarios are super useful, but in these places, they are actually harmful, because We… we write manual instrumentation, not the real SDK instrumentation.
Ankit Singhal 00:51:43 Let me see. So, I was… so line 97, right? Session that sent real-time input, so this is where I would assume that, okay.
I'm sending something over there.
WebSocket connection, and that's where, like, model will start.
Responding to this, right?
Would that not be the case?
Liudmila Molkova 00:52:07 Y-you… first… from what I've seen, at least in Google, that you send a continuous stream.
the user stream is continuous, and this is what the LangChain people are… Talking about User just talks continuously.
Do you still have it running? No, sorry. User just talks continuously, and model decides what are the actionable things.
From the stream, and this is how you interrupt the model, because you are already talking.
Because your stream is active, and model receives it.
Ankit Singhal 00:52:47 Yeah, like, as I'm talking to the model, it's gonna finally detect, like, if I have… stopped speaking, it's gonna detect that, okay, the user has stopped speaking, and then it's gonna start doing implants on the input it has received, right?
Liudmila Molkova 00:53:01 Yeah, and the only way it can do this is if it keeps continue… if it continuously receives the stream from you.
Trask Stalnaker 00:53:11 Due to the complexity of this, and Liudmila's, really good point about the reference instrumentation, not really… May not be the best way to validate this. Would it make sense to do a POC?
in the Python GenAI repo for, you know, both Gemini and OpenAI, for example, just… just a POC, not something that has to land, but something that, you know, gives us all something, like, hands-on that we can really use to validate, in code.
Liudmila Molkova 00:54:00 We can actually use RISE, the Open Inference, it has real-time instrumentation for OpenAI agents.
Cool.
Ankit Singhal 00:54:14 Bennett, exactly.
Trask Stalnaker 00:54:16 Take… take it in that direction.
Ankit Singhal 00:54:19 Yeah.
Trask Stalnaker 00:54:19 Yeah, we've been…
Ankit Singhal 00:54:20 That's what it depends.
Trask Stalnaker 00:54:21 I've got… I was lost, like, 10 minutes ago, and I want to try to help and follow along, but I think having some… the real POC would… is sounding like… I was thinking that I could use the reference instrumentation To get that clarity, but, it sounds like it would be better as a real instrumentation POC.
Ankit Singhal 00:54:49 And, Liila wanted to request, like, would it be… I would be, like… it would be very helpful if you can also, like, read off signs or two, because of some of these open things.
To kind of just make the decision on the… at least on the higher levels of planet, if it's secure, available, or… Open, we can set up something that'll, I think there are definitely some good points that you have brought up, which I think probably needs… Good understanding, and see on how they apply it to the right.
Most of the… and I think this is also, like, going into the trade of, like, how this applies to voices and so forth, like, not just in French, but…
Trask Stalnaker 00:55:35 I feel like the POC would, give a chance for other people, maybe, to participate more.
Ankit Singhal 00:55:44 Yeah, definitely, definitely. To do that.
Trask Stalnaker 00:55:45 first…
Ankit Singhal 00:55:46 Yeah, yeah. Yeah, actually, I just wanted to understand, like, the pieces that I think probably are missing here, so that I can kind of look into those more closely, and then put those details in the PR as well.
Looks like for the GenAI scenario, probably that things… If not, like, fully missing, but there are things that are kind of… Certain gas settings are referring to.
Which I think has a funnel.
Understand more closely and kind of work on those.
As part of this group. I think…
Liudmila Molkova 00:56:20 I think that the immediate and obvious step is to investigate what Open Inference has done for OpenAI agents, for OpenAI real-time.
And I have some comments on this, but I have some concerns about its stability, and they are faking spends, obviously, dear. This is my main concern, but, like, if you look into what they've done.
And, model what you want to do, accordingly, and you, like, if you find any issues with it.
And this would be the POC. It can exist in… as a pull request, the draft pull request, to Python GenAI.
Ankit Singhal 00:57:04 Yeah, I think it was gonna be, you mentioned the open interest, right? Other stuff?
That's it.
Liudmila Molkova 00:57:11 Awesome. Yeah, we just have 30 minutes left, I'm sorry to well, So, we have one update from Aaron, the main agent.
Aaron Abbott 00:57:25 There's not really an update here, I just was kind of bumping it again, I think.
There was, some changes requested, and Lududmil and I both maybe made some changes, so… Yeah, I don't know, it's just kind of a request for another review.
Trask Stalnaker 00:57:42 Can you, if you scroll down to the bottom of the conversations with Ludmila.
The PR dashboard comment.
I think it was near the bottom there. Thinks that it's waiting on author.
If that's… that looks probably invalid, so just… if you expand that comment of what to do if, like, doesn't look right.
Yeah.
If anybody, yeah, thank you.
That'll route it.
I'm… more and more, I'm using that, because my GitHub notifications are almost useless, so, it's… yeah, if people, just in general, can check that on their PRs, that it's getting routed correctly. And do open an issue if there's something that you see that's obviously wrong with that, PR dashboard routing. I've been fixing It's kind of whack-a-mole.
Liudmila Molkova 00:58:50 Yeah.
We have one minute left, Manish,
Mohnish 00:58:54 Yeah,
Liudmila Molkova 00:58:55 You want the Salesforce?
Mohnish 00:58:56 Yeah, it's pretty similar to what Aaron said. The changes that were requested for the reference scenarios, I'm not… I've dropped some of the fields, like version, which is not compatible by any of the evaluation models, and For the other things, which was hard-coded in the previous, comment that I made, I've removed the hard-coding, and then I've instrumented from the, details, so I would like to… I would like to have you a look, in the scenarios, like, the deep well, the DSPY. The DSPY was a little challenging because it was, it didn't have a lot of details, but, for the deep well and the Azure AI evaluations.
I've included a lot, so…
Liudmila Molkova 00:59:40 Yeah.
Mohnish 00:59:41 Yeah, and the file that Trask shared with me, the skills.md in the last meeting was really helpful on what to have and what not to have, so yeah, I followed that file pretty much on the reference scenarios.
Liudmila Molkova 00:59:57 Okay, awesome, thank you.
I'll take a look.
Trask Stalnaker 01:00:02 Thanks, everyone!
Liudmila Molkova 01:00:02 See you around.
Trask Stalnaker 01:00:04 Bye.
Ankit Singhal 01:00:05 Thank you, bye.
