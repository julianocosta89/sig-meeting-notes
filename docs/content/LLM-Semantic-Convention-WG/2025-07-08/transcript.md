SIG: LLM Semantic Convention WG
Date: 2025-07-08
Duration: 137 minutes
============================================================

## Zoom Recording Transcript

Giovanna Carofiglio, Cisco 00:00:49 Hi! Everyone.
Ridhima Satam 00:00:57 Hello!
Giovanna Carofiglio, Cisco 00:00:58 Hello!
Samuel Colvin (Pydantic) 00:01:00 Hi! There!
Josh Bonczkowski 00:01:01 Hello!
Liudmila Molkova 00:01:54 Oh, hello! Hi! Everyone!
Samuel Colvin (Pydantic) 00:01:59 Hi! There!
Liudmila Molkova 00:02:01 A lot of people here today.
Nice.
Okay? Quick question.
Ridhima Satam 00:02:11 I have a new pr to present here. Do. I have to add to the meeting notes? Somewhere in the next topics.
Liudmila Molkova 00:02:18 That would be wonderful. Actually, thank you.
Ridhima Satam 00:02:22 I'll just add it in the end of the Prs.
Liudmila Molkova 00:02:31 Okay, I'm going to start presenting. Feel free to add your things into the agenda.
and we'll get started.
Samuel Colvin (Pydantic) 00:02:41 Sorry, Ludmilla, is there a new? Okay, you're doing it now, I was going to say, Is there an is? This is the right document. It's not that we got a new one.
Liudmila Molkova 00:02:48 Yeah.
Okay?
So let's see, we had some discussions on the project planning last time where
talked about big areas. I'm looking for what we
should carry over from the last discussions.
Okay, we have some link chain instrumentation. Pr, wonderful.
Okay, I'm going to bring this one in.
And I think this one is a merge. So we can. Happily, let's forward.
Okay?
And let's put project priority is planning.
Do we have anyone who works on the multi agent stuff shipra, Sergey, do you want to share anything? Do you want to add something to the agenda.
shiprajain 00:04:19 Yeah, it'll be a quick update today.
so I mean, we will not have a a deep dive. So basically past past week, both the teams from Cisco and from Ms. We spent time in going over each other's proposal and building the understanding on the commonalities and the difference. We kind of finished off with our quick documentation and notes on that today and exchange with each other. Now, the next step is to get into the calls and proceed towards convergence.
Liudmila Molkova 00:04:53 Okay? So essentially you, it's that that's it. We we don't need a special item down the agenda. Or do you have any questions, any concerns.
shiprajain 00:05:02 I don't have any so we can hear from Pawan as well. He's in the call.
Pavan 00:05:11 Oh, no, nothing from my side.
Liudmila Molkova 00:05:15 Cool.
Okay? So then, let's get started. If anybody has anything to add to the agenda, please go ahead.
Let's take a super quick look at our project board.
Oh, okay, we have new issue
into one span kinda as one definition.
I think some generic discussion on the semantic conventions and whether we should have
one definition for span and Yaml multiple. I'm going to pass on this
dumped particularly. Believe it's the Gen. AI issue.
Okay?
So we've done the update on the multi-agent stuff
ratima. Did I pronounce your name correctly?
Ridhima Satam 00:06:22 Yes, that's right.
Liudmila Molkova 00:06:24 Okay. Nice. Do you want to talk about the lunch and instrumentation? And do you want me to present, or do you want to present.
Ridhima Satam 00:06:31 Yeah, I can present, I can share.
Liudmila Molkova 00:06:34 Awesome.
Ridhima Satam 00:06:53 Can you see my screen.
Liudmila Molkova 00:06:55 Yep.
Ridhima Satam 00:06:57 Okay.
okay? So yeah, so here's the Pr for the Langchain instrumentation framework under general, we're just starting with this. And we have some files which are just the skeleton files
we took inspiration from the open. AI v. 2. Instrumentation already there in the
in the instrumentation. Gen. AI. So these are just the basic instrumentation files the basic product project file. So we don't know yet, like, how do we want to go about this? So one feedback from that, like from the committee, that how we should be approaching with the 1st pr, like, do we want to add some business logic to it do should we support any feature in it? Because right now it just the bootstraps files we have added here.
Liudmila Molkova 00:07:53 Okay. Sounds good. Do you need to review from the
A. Gen. AI approvers and python.
Samuel Colvin (Pydantic) 00:08:02 We shouldn't be supporting 3.8, because it's deprecated.
I know that's a silly one line review, and I will review it. I can review it. I just noticed.
Ridhima Satam 00:08:12 Okay, yeah. So yeah, we just want to get it reviewed and want some general feedback on the
yeah.
Sergey Sergeev 00:08:21 Yeah, but basically, and we have the question, we have that feature branch where we implemented a lot of things with code. But then we got an idea that we need to make those incremental changes.
So the question to this group is, How do you want to proceed, or what are the processes, Aaron, I know that you are on both 6.
Aaron Abbott 00:08:51 This is good. I'm gonna take a look. Thanks for doing this
one thing I wanted to. That comes to mind is the package name
you might want to sync with near. I don't know if near's around today, but
we're able to kind of share the package name between open elementary and
the contribut repo for the vertex instrumentation. And hopefully, we can do something similar from this one. But
I would definitely just get in touch with him, maybe on slack.
like a DM or something. But yeah.
Sergey Sergeev 00:09:22 Yeah. It was the second question from redeem, I think.
Ridhima Satam 00:09:29 Yes, so we have the same question like, Do should we? Should we go? Be going with some other name, or
like? I see that in Openai they have
appended like v. 2 to it, like hyphen, v. 2. So that's 1 option. Or is there any other option like? If we use the same name, and we can still publish it. Are there
is there any provision for that.
Liudmila Molkova 00:09:55 Yeah, we will need to discuss with the was near trace loop they currently
own up in telemetry instrumentation, long chain package name and pipi
I can. You can start the thread on the slack channel. You can just ping him. And we're if if you need my help. Let me know. We can discuss with him whether the
would be open to letting us publish.
Together. So what we do for Vertex and Aaron, correct me if I'm wrong. We publish
vertex instrumentation. V. 2. They still publish to the same package name. But version 0 point something
we can ask near if they're open to doing to do the same for linking and
if yes, then we will just put the version to 2.
If not. Then we will probably do the trick with Dash v. 2.
It's ugly, but that that's what we can do.
Sergey Sergeev 00:11:04 Yeah, the challenge is that this pull request is just a skeleton, so it does not have the functionality needed. So if we publish in the same namespace.
so it will be discoverable code.
But it won't have any relation to the actual Pi package. People install so.
Liudmila Molkova 00:11:30 It's not a problem until we actually release right? So we can publish with this name.
I guess it's actually up to our. And I'm going to differ between we yeah.
Aaron Abbott 00:11:47 Yeah, my preference would definitely be to avoid the V 2. In.
Yeah, like, like, I, I don't have the keys, so to say, I think should should
just get in touch with near. But
yeah, my preference is to avoid the V 2, because there's already a lot of instrumentations, and I think it it just kind of distracts. And then this captures that you know the merging, if they use the same package name. So.
Liudmila Molkova 00:12:18 Cool. So then, assuming this pr is fine,
the python, 3, 8 is an important one.
There is. There are no blockers
to merge it, and then the features can be added incrementally.
Ridhima Satam 00:12:38 Okay. So I'll just wait for the feedback from other people like, is there any need to have any other changes for this like any basic changes. And then we meanwhile, we can also talk to need about it. But anyways, we can go ahead and merge this if everything is okay.
Now, because we can anyways
fix the name conflicting later as well. Like, you said before the release as well, right?
Okay, great. Yeah. That's all I had to ask, Sergey. You have any questions, other questions.
Great thanks, thanks.
Liudmila Molkova 00:13:21 Cool.
so let me start sharing again. Thanks for working on this.
Let's take a look.
Oh, sorry I'm I'm in the wrong spot. I'm so sorry.
Okay, the big Pr, we've been discussing for a while on how to record chat history.
So quick, update for everyone. So we went back and forth on
how to capture prompts and completions. We think we're settling down on the format
it will have attributes for input messages and output messages, and this attributes can appear on spans or events.
both
in in some edge cases we have some guidance on when to use spans when to use events. The
thing we
I think, stuck on is the uploading process. So one of the things I hope to resolve is how to store the content of the chat history somewhere else, and maybe put the reference to this content. I had a long discussion last time we talked about whether we want to store this data altogether like the all the input messages together, or we would rather store the
let's say, just the content. That's large and maybe sensitive.
we, it seems we don't have a consensus yet. So what they've done in this pr.
I've removed the rough part.
I need to update the description, but the Pr itself is no longer has refs.
There are still sections on the uploading. It's just unspecified how
my intent is to if and once it's merged to keep discussing the refs.
But I I'd like to make progress on on this pr without drafts first.st
So if we look here so what we have is, I have this attributes.
Where?
By default we don't record them.
If user enables content. We record them.
We can record them on on spans. We can record them on events.
We can upload the content somewhere. But how? What uploading process does is is not yet specified. And there is a to do. Item, this is a doc in development. So I
feel it's reasonable to keep it to do there.
Any immediate concerns with this one?
Yeah, Aaron.
Aaron Abbott 00:16:52 Not a big concern, but I just wanted to check the status of the event, body being turned into just attributes in in like the General Hotel spec.
Liudmila Molkova 00:17:04 So from semantic conventions, and from the spec
event, attributes complex event attributes are totally fine.
We are still moving forward with the complex attributes on spans.
We just had a spec call. And essentially, the debate at this point is around, okay.
do we actually allow it on metrics, or we don't, or entities, or something like this. So
it's moving when it's going to land. I I don't know.
Aaron Abbott 00:17:44 Okay? And then also, I think there was, there was an issue. I don't know if it was finalized for
getting rid of the log entry, body, field, and just having complex attributes, right.
Liudmila Molkova 00:17:57 Yes, we are actually doing it here. We don't use body anymore.
Aaron Abbott 00:18:05 Okay.
Yeah, just just speaking as like Google consuming the data.
I think we would put it in our like log body thing in our in our internal storage format.
so I guess it kind of depends. Like if if we're getting rid of log entry, dot body and hotel, then that's totally fine, like we'll we'll figure out a way to do the mapping. But
Bob
is there, I guess. What I'm wondering is, is there any way to know, besides consuming the semantic conventions, that
this thing is high cardinality or not, not like a label kind of typical attribute, use case.
Liudmila Molkova 00:18:46 You? Well, first, st we are not getting rid of the log body in in Otlp level. We are just stop using it in semantic conventions
you can distinguish those by the type. Right? So these are the regular attributes.
And if for some reason you don't want to store complex attributes and labels.
The Otlp will tell you that it's of a key value list, something type.
Does it sound right? Sound good?
Aaron Abbott 00:19:23 Yeah, yeah, that makes sense.
Okay.
Samuel Colvin (Pydantic) 00:19:27 But.
Aaron Abbott 00:19:27 Sorry. That was a little bit off topic, but.
Liudmila Molkova 00:19:29 I'm sorry no worries.
Samuel Colvin (Pydantic) 00:19:31 While we're off topic, and as a much smaller consumer, but still consumer of the data, what's the what's the process for
supporting this like across the ecosystem, so presumably does it does
long term. Presumably there need to be changes to the Protobuff definitions to support complex attributes. Presumably they need to be? No, so it's it's just a semantic, because at the moment they can only be strings right, or or a certain a small set of things.
Liudmila Molkova 00:20:03 So on the partner level, they can be anything on any signal.
the product level. They are complex, regardless on the Api level. That's a different story.
Samuel Colvin (Pydantic) 00:20:15 in at the protobus level. It's already can be complex. So in technically our code that our rust code that, like processes, the protobuf should already cope with the case of complex, or shouldn't be too hard to extend to do that.
Liudmila Molkova 00:20:30 I think you're you're back end already. Deals with them somehow.
So we've done some somebody told us that you're storing them as Jason and native support.
Samuel Colvin (Pydantic) 00:20:48 Yeah. So we already like the back end already supports it because we're already going from strings. We're parsing them as Json. But like.
I'll check with the database team. That's fine. Don't let me distract this meet this call.
Liudmila Molkova 00:21:02 It's good to know. This is the big company.
Samuel Colvin (Pydantic) 00:21:05 You post that link into the into the chat, just so that.
Liudmila Molkova 00:21:08 Of course.
Samuel Colvin (Pydantic) 00:21:09 That is okay.
Thank you.
Liudmila Molkova 00:21:17 Thank you.
Okay. So I actually want to spend some time today.
Discussing any open questions on this Pr
and checking. If we can make progress on this.
I'm going to scroll and see if they're open discussions, and I'm going to talk about them.
So, Aaron, do you remember what it was about.
Aaron Abbott 00:22:04 Well, I think you've removed the rough. So it's probably
okay to resolve it, for now.
I think the question was, was more like,
do do consumers know when one would be populated at the other? Or is it just a configuration option. And it's kind of up to the user to decide.
Liudmila Molkova 00:22:28 I see.
Aaron Abbott 00:22:31 Yeah.
Liudmila Molkova 00:22:32 So I would imagine, as a back end. You either support both, or you tell your users what to do.
And you're this troubled for configure. Stuff.
Yep, it's it's.
Aaron Abbott 00:22:46 I think it's reasonable.
Liudmila Molkova 00:22:55 Okay?
So then let's resolve this.
Okay, we have a
I I hope somebody can. Can somebody please send a pr, that that's 2 definition. We are getting questions about 2 definitions about
every week, and we just need to define them.
And I'm drunk.
Alex Hall 00:23:24 With the zoom.
Liudmila Molkova 00:23:25 Oh!
Alex Hall 00:23:25 Be easier to like. Stick them into here
like it's it's it would be nice to build on top of this.
Liudmila Molkova 00:23:33 What? What would? Why would we put them in the chat history? They are a separate attribute. Now you you would probably control it separately, you would consume it separately.
Alex Hall 00:23:46 It's like system instructions. But fancier.
Liudmila Molkova 00:23:50 And system. Instructions are a separate attribute.
Alex Hall 00:23:54 No, there would be a separate attribute. But I'm saying that they would be part of this whole thing of.
you know, the new structure of putting big things on spans instead of events, and so on.
Liudmila Molkova 00:24:05 Yeah.
so it's just a new attribute it. It would be straightforward to define one. I would assume it would have type any.
and I don't know if we want to go into the details of defining the
the 2 definition structure. That's a uniform across everyone. I don't see the point, but maybe.
Samuel Colvin (Pydantic) 00:24:24 Yeah, I see what you mean. I think they have a pretty.
There's a pretty simple definition of like
name description parameters, which is almost always Json schema object. So
not that I'm volunteering to to do it, of course, but I agree doesn't sound too difficult. Assuming that any type doesn't like that. We can use any type in you know, in a Pr
without this. This doesn't like we don't need any other work before you can like, just say, it's type any.
Liudmila Molkova 00:24:57 I'm
going to ask for exception and allow any on Spence and semantic conventions. I I might get pushed back, but
Samuel Colvin (Pydantic) 00:25:08 We should, we should review review this because I was just checked with Alex. And we haven't really reviewed this, so we will try to review it.
Liudmila Molkova 00:25:15 Wonderful.
Yeah. So then, please take a look. I think we're super close to the
having this part of work fully agreed upon and merged. So
if you can, if you can take a look that would be wonderful.
Samuel Colvin (Pydantic) 00:25:37 Yep.
Liudmila Molkova 00:25:40 Awesome. I don't see any other open discussions, and I I will wait for them to appear. Thank you.
Samuel Colvin (Pydantic) 00:25:49 I doubt we're going to have big issues with it, but I will try to get to it tomorrow.
Liudmila Molkova 00:25:54 Thank you. Tao, go ahead.
Tao Chen 00:25:58 Yeah, I just have one question on this. If we're putting the chat history in the span, how are we? You know, going to deal with the
the size limitation on the spend on the back end.
Liudmila Molkova 00:26:14 Yeah. So that's why we there is a second part of this work we didn't precisely agree on yet.
So if the content is too large, sensitive.
We would ideally not even store it
an observability back end to store it in some way. That's
that has different permission access model.
So ideally. What I would love us to do is to provide either custom, hook or standard eventually standard solution. Where we say, Okay, this is the prompt. This is the chat history.
Instrument like the the instrumentation code.
with some user provided hook, we would upload it somewhere, let's say, azure storage Amazon, s. 3. Wherever
and instead of recording this thing, we would record
the link to this thing or inside this thing, we can record links to, let's say images. We will record links to maybe large text
to the prompt. Maybe you have external system where you store prompts. Maybe you already have the link to this prompt
somewhere.
Tao Chen 00:27:40 So that's the approach.
And and that part of the work is still in discussion.
Liudmila Molkova 00:27:47 Yeah, we couldn't agree on how the granularity of what we want to upload. And it's just I'm removed it from this Pr to take smaller steps and merge what we can agree upon, and then
my next step is to proceed with to try to resolve and decide how we can do this.
Tao Chen 00:28:11 I see, I see. Got it. Thank you so much.
Liudmila Molkova 00:28:14 Yeah, thank, you.
Samuel Colvin (Pydantic) 00:28:16 I saw somewhere in your this document. It said to do on streaming, what is the state of?
Yeah. The situation on streaming chunks.
Liudmila Molkova 00:28:28 I?
Well, so the reason I put it here is because we had some confusion around. If I'm proposing to record attributes on streaming chunks. No
streaming chunks are probably logs or events, because they happen at a certain time, and this time is important.
So for them we would have to define some chunk event. Right? We would define the structure for the chunk. It would probably be very similar to the thing we have for input messages.
Sorry output messages, but chunked
right? And we would define an event per chunk. It probably needs some language around. Okay, if you're using up an AI, and the chunk is one talking. Do you actually want this event? That probably should put the big warning that you probably don't.
But for I think vertex where chunks are bigger, it's totally reasonable to enable those.
Samuel Colvin (Pydantic) 00:29:36 Yeah, I presume that
the what people will commonly want is is to basically bung them into messages and then them end up in the same format in the database as this. But whether, like, presumably that can be implemented by
maybe that can be implemented later, as in, we just like, yeah, basically.
group them into a list and put them into a into a span at the end.
because then you get the same format all the way across. And all you just yeah, you don't get to see the individual timings, but
it's gonna it'll it would work. It would probably solve the problem in in many cases.
Liudmila Molkova 00:30:17 So they are saying that
we can capture chunks as a list of things, and they could also have timing right. They could.
Samuel Colvin (Pydantic) 00:30:28 In theory, but I mean I don't know that the timing is once you want timing, I agree that there's a thing for that. It's called events.
I'm saying, though, if you
I don't know, I mean also, most of the models have a completely different format for streaming, so it might not be completely trivial to go from anthropic
streaming chunks to.
You know it's different. It's a different piece of logic to go from anthropic, streaming chunks to Gen. AI. Messages as it is to go from anthropic standard chunks to, you know.
Liudmila Molkova 00:31:01 Maybe there is no point on unifying chunking format, because it's a deep, debugging information that would. You would not use for anything except
some deep investigations. You don't need that unified.
Samuel Colvin (Pydantic) 00:31:15 What? No, you don't. Well, what you want. Is it unified in messages so that you can use all of your standard queries to go through messages, whether they were streamed
or not.
Liudmila Molkova 00:31:25 Absolutely. Yeah. So this is an incremental thing, right? You
want the buffered content more frequently than you want chunks.
Samuel Colvin (Pydantic) 00:31:34 Yeah.
Liudmila Molkova 00:31:35 And you can. There are cases where you want both.
Samuel Colvin (Pydantic) 00:31:40 Yeah, I'll have a proper review of the Pr. Sounds like the best way.
Liudmila Molkova 00:31:47 Yeah, sounds good.
Aaron Abbott 00:31:50 I'll also do the same. We'll take a good look. But
I do think it would be. I think we discussed like Json lines for the reference parts, and having these be lists of something
would be kind of a natural extension of that. And I I guess if it enables streaming. That's good, too. But I'll I'll read it and make sure. That makes that suggestion makes sense. But maybe we could.
Maybe we could do that in this pr. Too.
Liudmila Molkova 00:32:16 Yeah, if you have any thoughts on how we can incorporate those and make the streaming work closer, go, for it would appreciate it.
Oh, so moving on to the next one
I wanted to continue our project planning exercise.
So I I didn't convert but let's do it
So the we will do funny exercise of I'll share the doc
each of you has, let's say, 100 budget.
You can spread this budget. However, you like.
Among this items you can add items.
You can put 100 into one item. You can give each of them something.
However, you want.
The point is, you have a budget
and think about it as the time you would ride their group, invest
in the in a certain area.
Samuel Colvin (Pydantic) 00:33:43 Is it land graph as a separate row next to Langchain? Just because they're confused. They're like
same company. But like I feel like Langraft is. Maybe maybe landgraph requires multi-agent stuff, because that's all it really is doing. So maybe that's not true. But
I know it's just like
whatever our opinions are of them, that Langchain in particular, but also lang graph, have enormous usage compared to other libraries.
Liudmila Molkova 00:34:10 Right? So maybe we we can merge them
Samuel Colvin (Pydantic) 00:34:15 Yeah, I think they're quite different pieces of of work, I suspect.
But I suspect land graph is more like open AI agents in the sense that it's like
it's gigantic. And it's using like the the point is like with open AI. You get most of the visibility from the open AI live. SDK!
you might. If you're wanting agent stuff, then you want to instrument the agent framework same with Langchain and lang graph. You get most stuff from doing Langchain itself, but
you might also want to instrument the agent framework and
get the agentic observability that way. But those
conventions are far more nascent and less well established than than
even the ones on a single call.
I don't know what I'm.
Liudmila Molkova 00:35:05 Yes. So that
Sorry.
Samuel Colvin (Pydantic) 00:35:09 Go ahead, guys.
Liudmila Molkova 00:35:10 This.
so maybe we can break it down like this. So I don't want to single out every specific instrumentation.
But there are agentic
conventions we don't have, and we need. There are single agents, multi agents. There are just new instrumentation libraries.
Would this make sense, or you would rather have, like chainline graph, and maybe a handful of others listed.
Samuel Colvin (Pydantic) 00:35:44 I see the value in this, but I suspect that we have to. It's worth noting that
I don't mind.
Liudmila Molkova 00:35:55 Let's do this.
We don't need precision. We want to. I want to know what we want to work on.
Alex Hall 00:36:10 But hang on. What is this primarily about like? How we spend time in these meetings, deciding on conventions.
Liudmila Molkova 00:36:19 This is the plan for the group on what to focus on.
It's definitely questioned whether we have resources to work on it.
But I want us to come up with maybe I don't know 3 areas of focus
and actually make progress on the 3 areas.
And it means that if something else comes up we'll say, Okay, not yet.
Alex Hall 00:36:47 I guess what I'm wondering about is if the if the semantic conventions are already decided for something. Is it the group's responsibility to create implementations? Or is that just up to whoever decides to contribute.
Liudmila Molkova 00:37:05 Let's say, we as a group, decide that blank chain instrumentation is super important in line graph.
And now somebody comes and says, okay, I want to instrument that vector database.
I would say, Oh, okay, we are still reviewing this 5 Prs from the previous instrumentation that we're focusing on. So we are going to
pause on that vector dB, instrumentation.
Samuel Colvin (Pydantic) 00:37:34 Makes sense. I assume that there's a bit also of like. The big big organizations here will slightly, perhaps, take some influence. This will have some influence on what they allocate resources to.
Liudmila Molkova 00:37:45 Right?
Yeah.
okay, let the is the, does this make sense? Should we.
Samuel Colvin (Pydantic) 00:37:58 I mean my question, I guess, without making it an even longer conversation is what needs to happen on some of these, like Mcp.
as I understand it, I don't know where the convention is, but there's basically people put whatever it's called trace parent in Meta and call it a day
is, what more is there to do.
Liudmila Molkova 00:38:17 There is a bit of semantic conventions like how do you record to call? There are some discussions? Oh, you know what we record to call twice or 3 times in multiple layers, and and so on.
Samuel Colvin (Pydantic) 00:38:29 Yeah.
Liudmila Molkova 00:38:31 And most importantly, we have. I have a Pr. And nobody approved it. This is a signal from me that nobody is interested.
And that's fine, but I'm I'm kind of curious to know if if my understanding matches the reality.
Samuel Colvin (Pydantic) 00:38:48 Yep.
Liudmila Molkova 00:38:52 Okay. So what we'll do, each of you will get a column going to put Sam first, st Alex
around our please. I'm I'm just starting some names. So we don't get into the huge
conflict. And Google Docs. I'll put myself here, please add your name to the column.
and each of us gets 100.
Alright so.
and I'm going to sh share it.
And if you feel the
need to add one more item, I I guess that that's fine. We'll try to make sense out of this list.
and I'm going to paste it in the meeting chat.
If I can find it.
Okay, do your folks have a link.
Samuel Colvin (Pydantic) 00:40:24 Yes.
Liudmila Molkova 00:40:25 Okay, I see people.
Okay, I'm going to stop sharing for a sec.
And let's spend 5 min till 9, 46 on this one.
Aaron Abbott 00:40:48 Did you say we get a hundred points or 10.
Samuel Colvin (Pydantic) 00:40:51 100 column numbers in my column. Not to, if that's me.
Liudmila Molkova 00:40:55 Yeah. It's me. Sorry.
Samuel Colvin (Pydantic) 00:40:56 Okay. Good.
shiprajain 00:41:20 Ludnula, could you please share again? How do we number it?
Liudmila Molkova 00:41:27 So you you have a budget that's a hundred. You can.
Break your 100.
down. However, you want across this areas, you can put 100 to something. You can break them down by 10, or, however you want
it's just to get a sense on on
are we? What we are interested in that helpful.
shiprajain 00:41:58 Yep, thank you.
Liudmila Molkova 00:41:59 Thank you.
Samuel Colvin (Pydantic) 00:42:02 I changed the formula. I hope that's okay.
Liudmila Molkova 00:42:05 Yeah, sure.
Aaron Abbott 00:42:28 Maybe this is a stupid question. But is single agent instrumentation supposed to be including, like the inference bands that we that we're discussing still, and the remote storage stuff.
Liudmila Molkova 00:42:42 Oh, we don't have a a group refactoring, right?
I think those are slightly different.
Let's put the refactoring.
For existing conventions.
Samuel Colvin (Pydantic) 00:43:06 Is the blob storage not to be even more annoying? Does the blob storage stuff
deserve its own row or not?
Liudmila Molkova 00:43:15 I I just said it the wrong.
Aaron Abbott 00:43:17 Okay, perfect.
AB Austin Born 00:43:32 Hello
Liudmila Molkova 00:43:34 Yes.
AB Austin Born 00:43:34 I have never attended this working group meeting before. I'm a member of just an independent startup, interested in semantic conventions for opentelemetry, and I was wondering if you're open to me offering some advice as well.
Liudmila Molkova 00:43:50 Of course. Yeah.
The next ask, after we finalize this exercise would be, how much effort you folks want to put in each of these areas. It's just I'm keeping it separate.
Samuel Colvin (Pydantic) 00:44:34 Alex, do you know how hard it would be for us to donate our Openai agent instrumentation? Like open tree has done, or does it use logfire bits that are internal to us?
Alex Hall 00:44:49 Think not too hard. It's just been a while since I've thought about it.
We thought we would do it soon, and then got distracted.
Samuel Colvin (Pydantic) 00:45:00 Well, we're very happy to. If if there's I mean
if and when people want it.
Sergey Sergeev 00:45:10 Can you repeat the question? So you were considering to donate some parts of instrumentation or.
Samuel Colvin (Pydantic) 00:45:18 So. So we have an instrumentation of Openai agents
from when it very 1st launched.
but as far as I know, it's still up to date. We haven't had issues about it, but as far as I know, but that doesn't. That either means it's not being used, or it's good.
We would
be prepared to donate it as a as a package similar to the Langchain one we showed earlier rather than us, maintaining it within logfire.
Sergey Sergeev 00:45:44 Yes, it would be great, and to we from Cisco's Point side, will be very interested.
Samuel Colvin (Pydantic) 00:45:51 Okay.
Sergey Sergeev 00:45:55 And do you have this as a separate package, or you have?
It is part of the Openai instrumentation.
Samuel Colvin (Pydantic) 00:46:05 We have it in our logfire package, which is our
wrapper for opentelemetry. That adds a bunch of extra stuff, including this.
Sergey Sergeev 00:46:14 Oh, so so you have a single python package which basically instruments a lot of stuff.
Samuel Colvin (Pydantic) 00:46:21 Provides instrumentation. We don't turn most of them on by default. You have to enable them. But yes, as in
some of those things are very shallow wrappers around open telemetry, so like, if you do, instrument requests, I think we. We literally just call the the standard package for instrumenting requests. If you do instrument httpx, we add a bunch of stuff like capture all where we'll recapture the request, body the response, body, the headers and stuff like that
output instrument, or we have things like instrument. Open AI agents where we have the the. It's our implementation entirely.
But again, to do that, really, we need single agent
instrumentation conventions to be solidified, to be formula formalized before we.
There's really any point in donating stuff. I think.
Alex Hall 00:47:11 I mean, Openai already provides its own hooks for tracing.
It doesn't lend itself well to following any kind of semantic conventions unless they either happen to fit already, or we just ignore their hooks and
monkey patch ourselves like we do other things.
Liudmila Molkova 00:47:40 I don't want to interrupt this discussion. It's awesome. If
you're willing to donate open AI agents that that would be wonderful.
Samuel Colvin (Pydantic) 00:47:52 Sorry. Go on.
Liudmila Molkova 00:47:53 Yeah. No no go ahead.
Samuel Colvin (Pydantic) 00:47:54 But presumably there's not much point until we have single agent
conventions all done. Maybe that maybe I'm just behind, and they are reasonable. But the point is like the actual calls to the Llm. Obviously, Openai agents is using Openai. SDK, so
like you already get the like raw calls. It's the like
agentic stuff on top of that that like some stuff around tool calling.
That you would, you get from a instrumentation of Openai agents.
Alex Hall 00:48:31 I mean I don't. I don't know if it's worth
following the conventions is what I'm saying. That
open AI already like creates its own spans, not open telemetry spans. But you can. We make open telemetry, spans out of the open? AI is version of spans, and they, you know, they say, this is the important data to record
if we want to. If we need to follow, like some specific hotel agent, semantic conventions, then we can't really use that
unless they just happen to fit already, or we like, make open. AI,
follow those conventions in terms of what to record.
Samuel Colvin (Pydantic) 00:49:10 Making Openai do things is not easy.
So.
Alex Hall 00:49:16 Off, they create a span for guardrails, and so on.
Yeah, if we don't make conventions of those.
Liudmila Molkova 00:49:23 So we we would need conventions. That that's the. If if you're
if you have an instrument issue, you know what's the Delta is that that would be amazing to
see. And we have some things. So we have, like agent id and stuff.
there are some gaps. Of course we have in vocage and span.
We, we can record those there is there. There are Spence that we don't have. We either can define the conventions, or we can say, Okay, we will. We will add, dispense
once they are there for now, maybe we will just have to accept what open AI provides.
Samuel Colvin (Pydantic) 00:50:06 Also, Alex just checked. And we do have quite a few people sending us data from Openai agents. So I think it's.
I think the point is, it's working.
Liudmila Molkova 00:50:18 Oh, we have 10 min to play with the data, Sergey. You still have 5.5 points left.
Samuel Colvin (Pydantic) 00:50:24 Can you lend them to me.
Liudmila Molkova 00:50:28 It seems he's okay with it. He doesn't want to use that.
Okay.
so let's see, multi agents is leading.
Oh, thank you.
So all the agents.
and we probably the open AI agent,
Alex Hall 00:51:12 This relates to what I was asking about. There's already been a lot of talk recently about
people pushing forward multi agents and Langchain just in this current meeting. Like.
if we if we didn't vote for this, wouldn't this this happen anyway? Right?
It is not inevitable.
Liudmila Molkova 00:51:31 It's nice to have a confirmation for me.
Alex Hall 00:51:40 So what does it mean for the agent for the group to like put all its resources into this.
Samuel Colvin (Pydantic) 00:51:48 Well, I think there's, I think, as Lou Miller has said, there is value. We can. We can push a bit in some directions, and we can have some marginal impact on which bits get done. In what order? Based on
based on this? I mean, there's obviously harder questions like, is this, what end users is this, what developers want? Is this what
you know?
Yeah. But but we have what we have.
Liudmila Molkova 00:52:11 Yeah, for me, it's it's an interesting
Interesting findings are. I actually thought that evaluations would be higher and they are not.
Like also the new instrumentation libraries for simple models.
It's at 20. And it means that, let's say, when we talk about
open telemetry donation, actually, we care about length, chain land graph.
the open agents, maybe other specific libraries. But in general we don't care. We also don't care about vector dB, as much.
Samuel Colvin (Pydantic) 00:52:50 And we don't even care about land graph. I may say. You know, I was pushing to put land graph on there, because some people say, that's the, you know. That's their new thing. That's their recommendation. But it turns out
which kind.
Alex Hall 00:53:02 What's up?
Samuel Colvin (Pydantic) 00:53:02 Downloads.
Alex Hall 00:53:03 I'm just wondering, is it? Can we really be working on multi agents before single agent stuff like.
I agree with that.
Liudmila Molkova 00:53:13 It means that we need to finalize the single agent. But if we, if there is multi agent aspect, like context propagation between agents
it would just add another attribute or something, plus some context propagation stuff on top of single agents. So they're the multi agents. Yes, it's incremental. But it's also somewhat separate
parallel. We we can work on them in parallel.
shiprajain 00:53:45 Yeah, I agree, yeah.
Liudmila Molkova 00:53:54 Okay.
thank you for doing this exercise to me. What I want to do. I will post details on the chat. We don't have everyone. So I'm kind of curious if and how it will change if we ask why the audience in in the Gen. A chat
let's see?
But it, at least for me, puts a good mental model of what people are interested
in working on. I think it's valuable.
Okay?
And it's actually good to know that we're already working on this areas
like we have link chain contribution. We have a bunch of contributions for agentic stuff and ship Run. Sergey and other Cisco and Microsoft folks are working on the multi agent. Things
wonderful we have 5 min left.
Samuel Colvin (Pydantic) 00:55:04 Unheard of that we have time left over.
Liudmila Molkova 00:55:08 It's rarely happens does anybody want to talk about anything else? Or should we call it a day?
Samuel Colvin (Pydantic) 00:55:15 I just wanted to. If if with the last 5 min, something that I can create an issue to describe this. But I would love to get some initial feedback from anyone I know. I mentioned last week that we're working on Llm. Prices that is coming along, and we have a library that I need to make some changes, but we should have something up fairly soon. What we, what we, I think, are going to do is we're going to create logfire dot
cost.
which is going to be another attribute which will be a float basically, or, you know, decimal whatever to record a single cost of a span, and then we will have a logfire dot. Well, maybe we'll have log logfire. Dot cost dot amount, which is a number so it can be aggregated easily, and then we will have logfire. Dot cost dot details, which is, contains more details. So stuff like token cost of input tokens, cost of output token stuff like that.
would there be any interest in? I mean, I'm the one who normally says don't don't create the convention until you've used it and shown it works. So my proposal would be that we use this and showed it worked, and then proposed it as a semantic convention. Once we had some confidence that it actually covered most people's use cases. Obviously, it is not an AI specific, but 90 something percent of people's desire for it is to is to record the cost of Llm calls. So yeah, any feedback gratefully received.
Sergey Sergeev 00:56:41 Just wondering, why do you want to put it on a lockfire? Attribute name instead of just Gen. A.
Samuel Colvin (Pydantic) 00:56:47 Because we want to segregate things that were not semantic conventions, but are conventions for now, and I don't want to. It will be more confusing if it starts off being called Gen. AI, then gets changed when it actually becomes a semantic convention. So we namespace stuff like that. A few other things.
And obviously the reason that we we separate them out is the amount
in our database at least, is much easier to separate as a column and go and query on if it's if it's a like dedicated attribute than if it's in an any
Obviously, there's a world where you have multiple different costs per span, and you want to go and
run aggregations on a particular one. But we decided that the simplest thing to do was to say, really, you have one price per per span. And if you really want multiple different costs, then have multiple spans.
Liudmila Molkova 00:57:38 It. It would cover the the Gen. AI. Aspect right? If it talks to a database, you wouldn't care. It's on the Genie.
Samuel Colvin (Pydantic) 00:57:44 We allow we will allow people to. The point is here instead of us calculating it on server side, we're going to allow people to set that via the SDK. By default. It'll use our library to calculate costs of an Llm. But in theory, if someone wants to use it to calculate the cost of a like a call to Google's image libraries, or even like what? How much I mean? I suppose it's not cost anymore. But they could.
Yeah, they can use it for anything they want that has a has a cost.
In theory. They could go and make it like, how much did we? How much revenue did we receive? But then it wouldn't work, because that's not cost. That's income. But, like
the point is, it's it's and it touches on Aaron's point about the those open source projects to basically calculate. I mean, s. 3. You could think of that as another another case where, in theory, you might have object store costs. They're going to be very low, but they're going to be, you know, being able to aggregate them would be useful across a large number.
and then there's some complex interaction with how they become metrics, but I won't bore anyone with that, for now.
Liudmila Molkova 00:58:48 Yeah, so yeah, so essentially, the the intended use case is more like the generic namespace. That's not Jen AI at all.
Samuel Colvin (Pydantic) 00:58:57 I think if they became semantic conventions, then they should. Yeah, exactly. They should be called operation dot cost dot amount, or even operation dot price dot amount, because then you can make them negative. If it's
money going the other way in theory, or something like that.
I don't know. I don't know whether we want to get too far ahead of ourselves on all of that stuff. But the point is, I definitely don't think if it became a semantic convention. It should be Gen. AI.
I suppose the reason to make it Gen. AI is then interior. If you have 2 different costs, you can have a Gen. AI cost and another cost, but that seems almost unimaginable in reality. So
on a single span.
Liudmila Molkova 00:59:34 I mean, if it's the encompassing span like the one that describes rag, then you can have a breakdown. This is the database charge. This is the Llm charge.
Samuel Colvin (Pydantic) 00:59:47 Yeah, I suppose across a whole trace. You could imagine having the like cost of generating an image with.
you know
Google's Api, and you could have a Gen. AI cost and everything else. But then, again, even Gen. AI cost is already input is has about 7 different dimensions. But we're not capturing each of them as a separate monetary value. We're just capturing one cost, because we think that's
the best option for most people.
Liudmila Molkova 01:00:12 Yeah, we are out of time. I I like the idea. I also think that like
limiting the to the leaf spans the leaf client spans makes it much easier.
and then it it can have a clear meaning, cannot apply to both database and and Gen. A.
Samuel Colvin (Pydantic) 01:00:31 Okay.
Great. Thanks. Everyone.
Liudmila Molkova 01:00:36 Cool. Thank you.
See you later.
Aaron Abbott 01:00:39 Yes.
