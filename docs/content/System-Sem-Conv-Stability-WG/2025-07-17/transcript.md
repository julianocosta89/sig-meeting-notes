SIG: System Sem Conv Stability WG
Date: 2025-07-17
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Braydon Kains** 01:27 Hello!
**Pablo Baeyens** 01:30 Hey? Good morning.
you having breakfast.
**Braydon Kains** 01:46 Yep.
**Roger Coll** 01:53 Hello!
**Braydon Kains** 01:55 Hello!
**Dmitrii Anoshin** 04:10 Hi folks.
**Roger Coll** 04:13 Oh!
**Braydon Kains** 04:46 Are you waiting for anyone else.
**Dmitrii Anoshin** 04:49 Probably we can start.
I can just share some of this from my side. As I said, we want to introduce reaggregation option in data. Gen. So we can emit CPU metrics without.
like Per CPU attribute by default. So to reduce cardinality. And this, this is something that someone from my company, not from my team, but from another team, is working on currently. So.
**Braydon Kains** 05:20 Okay.
**Dmitrii Anoshin** 05:21 There is a promise there, and I'm working with him like helping with some questions, etc.
that pretty much on my side.
**Braydon Kains** 05:37 For me, I have.
I've updated the the Semcomf transition issue I don't let me. I'll put the link in the agenda.
So that is updated to the current state of things things the M data Gen. Thing we talked about last time I thought there was a bug in it. Well, there! Sorry there was a bug in it, but there was like a refactor that changed the code of like picking what templates to generate and stuff and that sort of like drive by fixed the problem, anyway.
So the bug doesn't exist anymore. M. Data, Gen can do everything that we needed to do for this specific part of the plan.
and so the next step is, I haven't found time to do it, but I'm going to do one of the scraper refactors just to like show what I'm thinking. And then we can base the rest of the scraper refactors on that And I also opened a collector, Rfc.
For something. That is where we essentially are saying it's required for the the merging of process and processes. Scraper, which is the the Wildcard name matching for metric builder configs.
The Rfc. Is essentially an evolved version of the original. Like Spec. For the matching that I had written in support of the implementation. Pr.
There are some comments on it, one comment that I need to address, that I haven't yet, but otherwise, for the most part. It is still like in a state where you could take a look at it.
**Dmitrii Anoshin** 07:31 Thank you, Brandon. I've been thinking that our original approach, when we can forward all those like Blob Glop from matching rules inside of the key.
I was like, after you know, uprs. I think it's maybe too much complicated. Maybe we can find someone another way of putting that somewhere, not in the key, but somewhere else, and have predefined key being like, I don't know some like, let's let's say, some hard-coded value underscore underscore some like I don't know match or something that does make sense, because putting that in a key kind of breaks our predefined configuration schema.
because our configuration scheme of the collector is kind of predefined is hard coded, and when you have this flexible kind of keys that that kind of break it breaks it. So I'm I'm wondering if we can maybe go a different route and maintain the like strict schema with moving this matching functionality somewhere else, somewhere.
**Braydon Kains** 08:56 Hmm.
**Dmitrii Anoshin** 08:56 Yeah, it's reviews. I don't know.
**Braydon Kains** 08:59 Yeah, that could work.
**Dmitrii Anoshin** 09:02 Because I believe that was the biggest complexity.
Don't know.
**Braydon Kains** 09:09 Yeah, the it was. It was the fact that the keys come in in any old order like, it's not a deterministic order. So I had to come up with a deterministic ordering based on the way the pattern was specified.
If we don't have that.
if we say we have like a a match config that's like a field of the metric builder. Config that will take the matches in an order. Then we could just use kind of any old wildcard matching like it doesn't really matter, so that could simplify it a lot.
**Dmitrii Anoshin** 09:44 I can't.
The other reason I'm bringing this up is because there is some another work by someone like it's like 3rd or 4th attempt whatever to actually make the configuration being defined in a yaml file.
Not so like we would generate our config interfaces from from Yaml, and from that Yaml. We can also generate the better documentation for our configuration interface, because it's it's likened at this point.
**Braydon Kains** 10:16 Yeah.
**Dmitrii Anoshin** 10:17 And it. It works fine as long as the configuration interface is like structured, predefined. But if we introduce this kind of wildcard, Martin, it's gonna it's gonna complicate the life of the person who is doing that much more. And I don't think we we will ever achieve that state when we can have.
like consolidated configuration, interface, and documentation being built from something from one source of truth.
**Braydon Kains** 10:52 Alright. Let me let me rethink that with with that suggestion.
I think, yeah, that would simplify things a lot doing it that way. So I'll try and find a a nice user experience for something like that.
**Dmitrii Anoshin** 11:07 When when we originally was thinking about that like when mandate was introduced, like in the beginning.
we were thinking about an option to enable or disable everything. So we were thinking like, let's say, special keys, something like dash, dash all or or yeah, something like that.
**Braydon Kains** 11:36 I think I had an issue open asking for that same thing actually.
**Dmitrii Anoshin** 11:40 Yeah. So maybe we can maybe start with that one at least, or in your Rfc, we can also bring some additional capability to introduce matching rules somehow following the similar approach.
Maybe someone else has other ideas as well.
And yeah, once you once you have the, we, we can chat about it, feel free to ping me in slack. If you have an idea we we can brainstorm it. Maybe we can even schedule a call. So if if you have time to share some of these.
**Roger Coll** 12:34 So probably maybe, Dimitri, that you are very familiar with. And I wanted to ask, because next week we have some free time with Damian that I don't know if you know him. It's it's also very involved in open telemetry. And we wanted to actually evaluate the overlap between M. Data, Gen and weaver. And just see if there's some kind of overlap and something that in the future we can unify.
And yeah, I just wanted to ask your opinion, maybe on that. And if you are familiar with both tools, or because I see that the issue that you just let's say, added to the document is actually, let's say, adding more core base in the M data. And that vision.
So so yeah, is that, let's say, impossible to be added in the weaver, or it's just another.
It has another purpose.
**Dmitrii Anoshin** 13:35 I'm not very familiar with Weaver, but I believe it's there is significant overlap. But there are still things that can be done with weaver. That cannot be done with M. Data, gen, some use cases covered in weaver and some use cases covered specifically with M data, gen, but not covered with Weaver.
So yeah, we can talk about it ideally. I believe we need one tool at the end of the day for sure. And that that's.
**Roger Coll** 14:02 Okay.
**Dmitrii Anoshin** 14:02 It's just how we want.
**Pablo Baeyens** 14:04 Sorry go ahead.
**Dmitrii Anoshin** 14:06 It's just how we bring, how we achieve achieve that state. That's unclear.
**Pablo Baeyens** 14:12 I was. Gonna say, there is a bunch of auto generated tests that are very collector specific, like lifecycle tests and stuff like that that.
**Dmitrii Anoshin** 14:22 Doesn't, don't really make sense in in weaver.
**Braydon Kains** 14:25 Yeah, I do think realistically like, like the you know, how weaver can generate for different languages, like realistically, there probably would need to be like a collector language which is not the right way to say, but like that's the concept, like they would need to be a completely separate generation, and it would route from the same like whatever we were configuration to generate any other language. But it would generate collector specific like, I don't think, because I don't think the go. The Go Cogen is gonna work for us at all. It's it's all SDK related.
**Roger Coll** 14:54 Okay, yeah, makes sense.
**Dmitrii Anoshin** 14:56 So I'm not sure. What's the scope of weaver like? What? What scope of use cases does it cover if it cover, generate, generating everything for every SDK. In that case we can have this, let's say collector language for weaver, if we were, is only supposed to be used for like metric and tracing, and all of that stuff. So in that case.
as Pablo mentioned, like lifecycle and everything doesn't make sense in, we were. In that case weaver can be used by the M data gen specifically for the matrix part, and like internal telemetry part, or something like that.
**Braydon Kains** 15:40 Okay, yeah.
I think the the best way to integrate it probably would be to keep Mdata Yaml, metadata, Yaml, and the Mda. Gen. Tool, but, like part of metadata, Yaml can be weaver configuration, and that will.
**Roger Coll** 15:53 Generated the weaver.
**Braydon Kains** 15:54 Parts of the Api under the hood.
I'm looking.
Probably it would be a mixture.
Yeah. And we can.
especially because metadata Yaml is also not purely for M. Data. Jen sake. It's also for various like Github, tagging automation stuff like code owners and other things like that. So it would probably like it would. It would like the weaver config would be like a subfield of metadata yaml, or a separate file, or something like that.
**Roger Coll** 16:22 Yeah, sounds sounds good. Yeah, that makes sense. Actually, what? That's what one of the ideas from Damian just calling. We were from M data, and progressively, just trying to to see all the, all the features. But yeah, that's really great insights. And probably the the goal that we have is just to, for now at least document it, and just see what what's in for each tool, because either of us is is familiar, and and probably that's it. I I will share the the output with with you.
**Braydon Kains** 16:58 The biggest reason I'd like Weaver is because it's sort of built for generating from semcomf definitions like those Semcon definitions that we have are weaver like.
**Roger Coll** 17:09 Yeah, exactly. I think the idea came from. I think one issue from Christos that he would like to add, let's say the same Comps reference in the code generated, but but by M. Data. So that's the the thing that we were seeing that it was overlapping. So.
**Dmitrii Anoshin** 17:48 Okay. If there are no other topics for today, maybe we can call it.
**Braydon Kains** 17:52 Yeah, I don't have anything. There was the. There's the Nfs and Raid Prs that are both going on, and I'm having trouble with both of them, because, a particular reviewer is really trying to like, do a lot like trying to like force, those to be unified with like other storage or other Rpc metrics and stuff. And it's making the design really like tangled and complicated. I'm not super liking the way those are going. If if anybody has time to take a look at either of those would be helpful. But.
**Dmitrii Anoshin** 18:34 Who? Who is that reviewer?
**Braydon Kains** 18:37 I think his name is James Thompson Thompson. Toma.
Does this Github handle.
**Dmitrii Anoshin** 18:43 Yeah, but like, are they part of any sick or or like.
**Braydon Kains** 18:50 They're in the Rpc. Sig. And I think they're in in one other sig. They do come to the semcom meetings and stuff.
**Dmitrii Anoshin** 18:59 Okay, I see.
Yeah, I I don't have expertise in those fields.
But if you, if you think I can, maybe.
**Braydon Kains** 19:15 Well, at the moment, it's it's more of a like a general Samantha conventions thing. So maybe I need to just bring this to the to the Sig next week, but.
**Dmitrii Anoshin** 19:22 Yeah, yeah, that would be.
**Braydon Kains** 19:25 Noticing this trend of like we're trying to force using shared metrics and attributes and stuff even where, like trying to superimpose it onto these conventions makes it very tangled and confusing.
**Dmitrii Anoshin** 19:37 Right? Right? Yeah, that that would be the perfect approach. If you can join. If you can raise that in semantic convention saying like, hey? It doesn't make sense. Let's maybe not go that.
Yeah.
**Braydon Kains** 19:54 I'm hoping I can get both of those merged, because now they're blocking more, more and more host metrics, viewers.
**Dmitrii Anoshin** 20:01 Yeah.
**Braydon Kains** 20:02 So alright.
**Roger Coll** 20:08 Yeah, on my side, just very quick. I opened this issue to change the definition of the used memory state metric.
Yeah, please take a look, because I know it's a bit controversial, because there's for now we had this assumption that all the States sum up to the limit. But if we change that it? It's not.
But it's not a little bit not like that anymore. So yeah, please leave your thoughts. There.
**Dmitrii Anoshin** 20:42 Interesting.
Is that the case for any other solution in in the industry right now? So if you aggregate by the state field, it doesn't sum up to one to the limit.
**Roger Coll** 21:03 I'm not sure for metrics, for in elastic what we have, it's like.
instead of modifying the the used because of, let's say. But this is for historical reasons, and and for being yeah compliant.
we added a new metric that it's called system dot actual dot memory, and that's the one that it's used in all the dashboards and all the alerts, and that's the available one.
**Dmitrii Anoshin** 21:31 But we yeah, we already have that metric in the collector as well.
**Roger Coll** 21:36 Yeah, exactly. Yeah, yeah.
**Dmitrii Anoshin** 21:38 So like from semantic convention perspective.
It says that if you aggregate over and attribute it should give you a meaningful result.
And now we are looks like we are going against that recommendation. If we, if we, if we change the source for that attribute.
**Roger Coll** 22:04 Yeah, that's right.
**Dmitrii Anoshin** 22:05 I was under impression that you said that in even in elastic, it's there is no like separate metrics specifically for that. It's being used as as.
**Roger Coll** 22:18 So yeah, probably I thought that it was. Let's say the used one. But we have.
So because of, let's say, backwards compatibility. We keep the used one historically, but it's not used anymore. So it's it's there. But all the let's say, the dashboards and other stuff, just another one that we call it actual memory and the actual. It means that it came from the operating system. It's not something that we built up that for more.
**Dmitrii Anoshin** 22:49 And then in that case we we cannot make. If we. If we make that change.
there is no way to make it so. It ends up after aggregation ends up and on to the limit.
**Roger Coll** 23:02 No, because, yeah, the we were able to do that aggregation because they used to state it's derived from other. Let's say states.
and it includes the total. So if you let's say, remove all the other States from the use.
you'll get the total.
**Dmitrii Anoshin** 23:20 Yeah. And that's from semantic conventions, from like, not even semantic conventions, but from telemetry specification. That's the correct behavior.
**Roger Coll** 23:31 Yeah, exactly. Yeah, yeah.
**Dmitrii Anoshin** 23:33 Diversion from that is, is a good idea.
**Roger Coll** 23:37 The thing is that what we prefer. Let's say, yeah.
a metric that can be misinterpreted, a state that can be misinterpreted, and it might lead to some confusion and and maybe provisioning.
But resources, or the actual one that it's recommended by the OS.
**Dmitrii Anoshin** 24:03 In that case it should be separate metric with no attributes. That's the open telemetry specification guidance.
If it, if aggregation over an attribute doesn't make sense. It has to be a separate metric.
**Roger Coll** 24:17 Yeah. But the thing is that this used metric. It was not provided by the OS, it's something that some guys build up. Some came up some years ago.
**Dmitrii Anoshin** 24:30 I understand. But but anyway, that that's the that's the idea. I believe you. It's not like pushing back. I believe you'll get push back from tc, about that change.
**Roger Coll** 24:47 Okay, yeah. So let's see.
**Braydon Kains** 24:50 I mean, is it fair for us to keep the original state, and then say so? This is only the case on Linux, right, like this same metric, if we, if we did it on windows, would actually be like the calculation was actually.
**Roger Coll** 25:06 Yeah, because.
**Braydon Kains** 25:07 Will use.
**Roger Coll** 25:08 In. So like.
you have a metric that it's available. That's the same in Linux, and we use that one. But in Linux, instead of using the available. We use the 3 plus guys.
**Braydon Kains** 25:22 Oh, yeah, right?
**Dmitrii Anoshin** 25:26 But in windows it properly adds up right.
**Roger Coll** 25:29 Yeah. Approval. Yeah, yeah, yeah. It's like a very edge case. But.
**Dmitrii Anoshin** 25:36 I'm curious about this, and there is a way to make it adapt on Linux as well.
**Roger Coll** 25:46 I don't think so with the current estates, because it it's very kernel specific, it it's a this metric goes through all the buffer memory, and and sees if it's dirty or or not, and the one that it's dirty can be used, the other one. It's not counted there. So then it's it's not the whole buffer state, it's a very special state. So if if you sum or or decrease the buffer or the other States, it go further further away there the limit.
So.
**Dmitrii Anoshin** 26:28 What are the States for the windows?
**Roger Coll** 26:32 Think it's.
And yeah, there's just a couple of states, I think.
**Dmitrii Anoshin** 26:38 Can we maybe replicate those States for Linux as well? There'll be less States, but it should adapt as well.
**Roger Coll** 26:46 That's a whooped area.
**Dmitrii Anoshin** 26:52 I would love.
**Roger Coll** 26:52 I'm just.
**Dmitrii Anoshin** 26:54 What what other life solutions do for that?
I don't know what like, maybe what maybe pop up.
**Braydon Kains** 27:04 It might be hard to find a solution that is trying to cover this exact same scenario on both Linux and windows, like our conventions are like, I think, a lot of system monitoring tools will just put like a windows, windows, specific shape for the metric, and a Linux specific shape for the metric.
I don't know that for sure, but that is what I'm what I gather, because, like the a lot of a lot of windows, memory tracking stuff is based off of like what task manager tells you to do. And a lot of Linux ones are based on what Top says, and they just sort of.
and come up with their own opinions based on that we might this, this it might not be true. There might. There might be something that exists, that is, that is trying to cover this exactly the same on both systems, but might be tricky to do that. I I wonder if maybe what we should do is keep.
Keep the memory metric with the like. It sums across the state attribute still sums up to the limit, but then, like, add a note that says, if you're on Linux, use this Linux specific.
available calculation that is a more realistic.
more realistic calculation of actual memory available.
This is this is still getting into this, the same problem I keep on having where we have to like, just because we're trying to follow semantic conventions rule, we have to put all this like really specific guidance in, just in like descriptions of metrics that makes it kind of hard like. It harms the usability of our conventions. But there isn't really a good, a good answer other than that.
I'm not sure.
**Roger Coll** 28:43 Yeah.
**Braydon Kains** 28:43 I think it, it comes down to the like. How valuable it is for us to to keep this metric usable and and aggregatable across the State to get the limit.
**Dmitrii Anoshin** 28:59 Yeah, it may be not useful. It may be not necessarily. But again, if we start the version from that, it would, it would be like, I don't know it. It's it's just open time. Specification doesn't make sense anymore. In my opinion.
**Roger Coll** 29:18 So.
**Dmitrii Anoshin** 29:19 This is the 1st thing source of truth when you like, read and understand how open telemetry is built, how is modeled? And then you have all of these like places when it's broken.
We either need to change the specification, saying, we allow exceptions. And here is the list of the exceptions, or we try to align specification.
**Roger Coll** 29:49 Yeah. But I think I liked your solution about just making a the 2. Let's say, 2 attributes opt out the like, the available. And they used as windows.
**Dmitrii Anoshin** 30:02 Yeah. Let's keep.
**Roger Coll** 30:03 The free and catch as opt in that would still sum up to the limit.
**Dmitrii Anoshin** 30:10 Yeah, potentially, we can do that. I would also maybe suggest to do investigation across the industry. See what the other on board collection solution do maybe what day to day, for example, or some others.
because they likely switched. They likely adopted that Linux capability, but how they adopted it. That would be a good exercise.
**Roger Coll** 30:40 Yeah, probably there isn't this assumption that all the States need to sum up to the limit in many.
in many vendors.
**Dmitrii Anoshin** 30:49 Maybe broken, but maybe not.
**Roger Coll** 30:52 Yeah, yeah, sure, I would check.
**Dmitrii Anoshin** 30:55 We we can. It's we are at time to jump to the other.
Thank you.
**Roger Coll** 31:01 Thank you.
