SIG: Semantic Convention Tooling
Date: 2025-09-10
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:58 Hey, Jossie.
How's everybody doing?
**Nathan Smith @ Elastic Observability** 01:21 Good.
**Josh Suereth** 01:25 Apologies, I was a little late getting started here.
So this is due… To the agenda…
**Liudmila Molkova** 01:47 Hello.
**Josh Suereth** 01:48 Hey!
I think Lawrence said he was gonna miss this meeting, as an FYI.
This week, so… We might get started. Jeremy's here, too. Good.
Alright, I'm not presenting, am I? Hold on.
**Liudmila Molkova** 02:07 No, you're not.
**Josh Suereth** 02:09 Okay, we're getting there, we're getting there.
Alright.
Cool. General discussion… Ludmila, I think we're gonna cover your CL in the Weaver Project Board, but that is the topic I would add otherwise. Let's check real quick. I don't think we have anything… New on the tooling project, I was actually thinking about this one, and we… I believe we're literally going through this improved YAML schema right now with V2, right? The long term and stuff. I wanted to ask if it makes sense for us to start tracking schema V2 work with these bugs and decide, yeah, we're gonna keep these, or no, we won't do them.
How do folks feel?
**Liudmila Molkova** 03:02 This is semantic conventions.
**Josh Suereth** 03:07 These are some intervention things, yeah.
**Liudmila Molkova** 03:11 I… Actually, I don't really understand the benefit of us separating these two. Well, I understand some of it, but, like, where would we put the schema YAML to work items? If we are changing semantic conventions YAML, then there, right?
But if we are just, implementing Schema V2, then it's Weaver Project.
**Josh Suereth** 03:36 Yep.
Yeah, I feel like, I wanted to look through here, because there's some things on here that we've been talking about with V2, right?
histogram bucket boundaries, I think, was mentioned briefly. Events metrics and resources supporting requirement level. Like, these are all things we have an opportunity to tackle with the V2.
Sampling relevant, for sure.
**Liudmila Molkova** 04:02 Right.
**Josh Suereth** 04:02 But I'm tired of looking at two project boards personally, so I'd love to shove everything into the Weaver project board, if people are amenable to that.
And we can… we can shut this one down and start using the Weaver board as our As what we do going forward.
**Liudmila Molkova** 04:21 Yeah, I would love to help with this.
**Josh Suereth** 04:25 Okay.
Cool. Let's do that. The only thing that I think we would miss on here… yeah, everything else has something in Weaver that is the same. The template generation… that lives in Semantic Convention's directory, or lives in Semantic Convention's repo and not in Weaver. That's the only thing that we would drop from the SIG that we might want to otherwise track and figure out.
**Liudmila Molkova** 04:57 We don't need to drop it from the board?
But we can drop it for, Well, what stops us from keep tracking this somewhere in the backlog? Because it's the feedback, right? To a certain extent, to deliver.
**Josh Suereth** 05:16 Yeah, yeah, I think this is, all of this… all of this is stuff I think we should actually work towards getting and fixing. I… what I'm worried about is every time I look at this board, right, and you look at, you know, things that are defined in tooling and… I don't feel like we're really using this board, and so it's not providing a lot of value.
It's a backlog of things we don't look at, so I'd prefer to do something about it.
Okay, Sounds like, these things… let's… if we talk about V2, we can walk through this, but I'm going to, for now, We'll move on to the Weaver Project Board.
And look at some of the issues and things that showed up lately.
And do a little bit of triage. And going forward, we'll figure out how to merge the… YAML v2, bugs into the Weaver V2 work. Sound good?
**Liudmila Molkova** 06:19 Okay.
**Josh Suereth** 06:22 Alright, so that was that. This one, we have to consider for next release and next release.
And I think, Lyudmela, did yours show up yet?
Is this… this is the bug that you fixed, right? Here?
**Liudmila Molkova** 06:40 Oh, I didn't create a bug, I just created the pull request.
**Josh Suereth** 06:46 What was this one? Oh, right.
Couldn't get the content during spans emptying attributes. This is something I need to triage later. Someone sent us a bug that we should, finish triaging. I think this is going to be ease of use bugs. For context, someone has a, they were running Weaver, and they were trying to generate, spans and, markdown, and they get, like, a successful output that doesn't actually have any data in it. Where's the error message? Here.
After placing signifies the model directory… yeah.
With empty no content. Yeah, so this is, like, debugging-related features, which… Might be helpful.
Might be helpful if we add, like, a, no signals match to your ginja filter or something, I'm not sure.
**Liudmila Molkova** 07:46 We now have this debug, debug works, and if we can… I can move a comment to enable debug output, and then we would see… what was the input to Ginger?
**Josh Suereth** 08:03 Oh, because we added the debug stuff, yeah, yeah, okay. Would you mind commenting on this, Camilla?
**Liudmila Molkova** 08:07 Yeah, but we didn't release it.
**Josh Suereth** 08:10 Okay. Okay, so we have the release, and then… okay, cool.
**Liudmila Molkova** 08:14 I'll make a comment. Where it bounced?
**Josh Suereth** 08:18 Let's cut a release that will include a debug feature that can help us figure out what's going on here.
I think we need better docs around debugging.
But we'll, reduce this.
Shield 2.
Track both.
The debugging feature… And fixing the, specific issue.
Okay, let's do that.
Cool. So that was one of the new ones that came in.
What else did we have?
This doesn't pull in pull requests, so I'll look at… I'll look at what you have, Lumella. I want to, I want to throw that in the next release column, though. Do you remember what the number is?
Fail when template doesn't match any file. There we go.
**Liudmila Molkova** 09:19 Yeah, 928.
**Josh Suereth** 09:22 Yeah, do you want to talk us through this at all?
**Liudmila Molkova** 09:24 Yeah, so Martin was playing with Weaver, he had the wrong name for a template file.
**Josh Suereth** 09:33 And apparently, we never fail on this.
**Liudmila Molkova** 09:36 The way we actually process templates is interesting. We take the directory where the templates are.
And we process each template one by one.
template files, the existing ones. So, if it happens to be that there is no template file, for some section of Weaver Config, it turns out we never actually, touch this piece of config. It creates problems like this, the confusion when somebody uses something wrong. So what they added is just the validation when the template engine is created.
that, all the templates mentioned in the Weaver config actually exist, match some of the files in the templates folder.
And that's it.
**Josh Suereth** 10:29 Yeah.
I think this seems like a huge win to me. It's also interesting how many invalid templates you found.
**Liudmila Molkova** 10:40 Yeah, and the corresponding task passes, and they validate the content, so… This was completely ignored.
I'm probably puppy based there.
**Josh Suereth** 10:54 Yeah, I think this is from when the Weaver prototype, when we pulled over.
the… Half the tests were removed because half the features were gone, and then we slowly added them back in.
Yeah.
Okay, cool. I'm… I… I would like to include this in the next release, if, anyone has concerns, let me know. Jeremy, or we can ping Laurent to get a review from another maintainer on this, that'd be good. Anyone have concerns with including that in next release?
**Jeremy Blythe** 11:28 No, I'll take a look today.
**Josh Suereth** 11:30 Okay. I think we probably… Do we need a description? Probably not.
Let's go back here.
To consider for next release, intermediate Registered Directory, optional, we'll check in with Lawrence on that one. Updating the new values when referencing attribute, I think this one still has somewhat of a design discussion going on, is that correct?
**Liudmila Molkova** 11:54 Yeah, but I really like the idea of limiting this problem as a first stop.
2… just the literal value. So, there is a huge genome.
And this particular convention only needs a single value. How do we, explain it?
So, I think there is some suggestions from James, on different options, I… I think this is the… either the naming or the taste questions more than the design questions, and I… I'm not… I don't want to fight about naming. We'll figure it out.
**Josh Suereth** 12:43 Yeah, I… I do think, Mike, the question I want to ask and resolve now is, do you think we should do this in V1 today, or do you think we should make this part of V2?
**Liudmila Molkova** 12:58 I think we should make it part of V2. I don't see any reason to make it part of V1. We can survive as the current state of affairs.
**Josh Suereth** 13:08 Alright, I'm going to… because we don't have it yet, we have ease of use, I'm going to make a new, backlog item for… V2 schema.
**Liudmila Molkova** 13:21 Jeez.
**Josh Suereth** 13:26 And then… Oh, come on.
For some reason, the web is really fighting me here. Okay.
I'm gonna move that one to… That wasn't ease of use, this one here.
I'm gonna move it into V2 schema.
Or not.
Come on.
Where did it go?
Okay, guys, I'll deal with this later. We'll just go through to consider for next release. Okay, Weaver should resolve full URL. This is where, we use absolute paths, and… this is, I think, about, the full URL when we have links.
And this is about generating Javadoc.
I think this might need some more design to it.
**Liudmila Molkova** 14:24 Yeah, probably.
**Josh Suereth** 14:26 Okay.
I'm gonna leave it in to consider for next release, and I think maybe we can, Do we have a need more? No.
maybe we'll get a label that says we need more design. Alright, so that's that. Was there anything else in here that folks felt strongly about that they wanted, document exacting? This… this work is still blocked on other things with JQ that I'm fighting with.
Exact date amount, 5 cents of ginja… That was all the ease of use stuff. Oh, sorry, not on the next release.
Generate JSON schema from Rust models.
Did we… I thought we had fixed this.
**Liudmila Molkova** 15:16 Did we?
**Jeremy Blythe** 15:21 We generate the models so that we get the… sorry, we generate the JSON schema.
As part of the process of… Creating the better error… error reports.
So if you put in invalid YAML, But what we… we stopped short of making that generated output.
The replacement for the handcrafted one that we have at the moment.
I want to do that in V2, because it… because of the way groups have got, like, a group has everything, and then you've got, like, a million options.
So V2, I think, Will give us the opportunity to correct this.
**Josh Suereth** 16:06 Okay, so should I move this into V2?
**Jeremy Blythe** 16:08 I think so, yeah.
**Josh Suereth** 16:10 Okay.
Alright, I'm fine with that. There's… there's a lot of… fun if we try to have the same JSON schema do V1 and V2 at the same time. I can show you how bad the error messages are, but they were quite atrocious.
**Jeremy Blythe** 16:26 I'm sorry.
**Josh Suereth** 16:27 I tried for a bit to fix it, and I failed. Okay.
That's a good one.
What else do we have? Template extension weirdness with Weaver Registry Diff. I don't think this one's been triaged to figure out what's actually going on.
**Liudmila Molkova** 16:43 Yeah, and I'm trying to remember what it was about.
**Josh Suereth** 16:51 Well, yeah, this is where it just randomly turns things into strings for some reason and doesn't otherwise.
**Liudmila Molkova** 16:57 Yeah.
And it only happens with YAML and with some default configuration, so it's essentially a bug, there is a repro, It only affects semantic conventions so far.
**Josh Suereth** 17:12 Well, I think, given that it's based on the file name, it could be… it could affect everyone, but that's, we still need to triage that one.
So that one needs to spend a little more time on. Output of Weaver Registry Resolve, drops empty fields. This, I thought… Was on purpose, right?
So we need to re-evaluate some of our serialization due to those restrictions, otherwise I think we can update pre… yeah.
So… This is where, we're dropping brief.
If it's an empty string, apparently.
I would like to update this one to basically say we should… and I think this is true in V2, we require brief.
And we don't ignore it if it's empty.
So, if it's empty, you get an empty string.
Does anyone have any concerns with that?
I think that also should be the case for, What was the other one he wanted? Register URL.
Okay, so this seems like an easy fix. This is something I might be able to actually get to relatively quickly. I'm gonna leave that into consider for next release, and we can go from there.
Alright, that's it for To Consider for Next Release. Let's go into our agenda. That was… spent a little too long triaging, apologies, so… Two bugs.
So we looked at our next release, and this is… Start merging schema fixes into U2.
Project Ford for Weaver… Start using Uber.
Budget boards, trap things… Instead of… Oops. Okay.
Update on attribute groups. Is this, Ludmilla?
**Liudmila Molkova** 19:14 Yeah, I added this too. Before I start, I see Jurassi here. I'm curious.
What brings you here?
I'm excited to see you.
**Juraci Paixão Kröhling** 19:23 Now, I think it's… well, instrumentation score, of course, right? So, I think there's… there's a few things, that overlap Weaver with instrumentation score. People have been asking. I… I think there is a great potential for collaboration, and I'm here to learn more about Weaver.
**Liudmila Molkova** 19:42 I…
**Juraci Paixão Kröhling** 19:44 I was hoping that other gardeners would join as well, and eventually they are gonna join. I think it is very important, for me, and for us to, to collaborate here, to contribute to the project. I think we are late already, but I think better late than never.
**Liudmila Molkova** 20:04 Great to have you. You're not late. Right on time.
**Juraci Paixão Kröhling** 20:06 Thank you.
Yep.
**Josh Suereth** 20:12 Awesome.
**Liudmila Molkova** 20:12 Okay.
Wonderful. So, actually, there is the item I want to discuss later about the life check. It's probably very relevant to instrumentation score.
Okay, so I wanted to talk about attribute groups, more like an update. I, Started, implementing, the approach that I think we eventually agreed upon, but I wanted to make sure we did. So, I had… I had some thoughts about having different concepts for a public group and internal groups, and maybe call internal groups makes sense, but maybe it's not… it doesn't make sense.
So, the thing I'm working on is to have attribute group that could be internal, could be public. We don't even need to implement public group in the first PR. We definitely needed to switch existing conventions to V2. But I probably won't implement public yet.
Internal groups will be removed from the result schema, they don't exist there.
And it all works… Nicely, until we get to the sampling relevant, right?
So, josh, you have some thoughts? I… my thoughts are the following. Let's… let's make any group support sampling relevant. Like, you can have attributeRef that supports sampling relevant. Any attribute ref can support something relevant.
But if you use sampling relevant on signals that don't support sampling, we will fail.
**Josh Suereth** 22:12 So, so I've, I have two… let me, let me just outline my two concerns, right? So, one is that, Sampling relevance is always filled out for spans, right?
And, sampling relevant, isn't accidentally inherited.
That's it.
**Liudmila Molkova** 22:35 Oh, always filled out.
Probably, it's impossible to… Detected in any way, so some attributes on spans would have something relevant.
**Josh Suereth** 22:47 That's… that's basically what I mean. Like, on a spend, you need to always have some attributes of sampling relevant.
And I want that to be kind of natural and easy and enforced.
And if the syntax forces you to do it.
That's the… that, I think, is the strongest way to accomplish that. The other option is we could have, like, something which detects when you have a span that does no sampling relevant on it, and yell at you and say, hey, this span has nothing relevant for sampling. Is that really what you intend?
**Liudmila Molkova** 23:17 Wait, can we even have this policy?
let's say… well, we don't have spans without attributes in semantic conventions, right? So, yeah, I think that's fine, yeah.
**Josh Suereth** 23:28 Yeah, yeah, but that's basically the issue, is, okay, so if we're going to have sampling relevant be part of an attribute group that can get used across signals.
It means that I might define an attribute group for metrics and not put sampling relevant there. Then I might reuse it in spans and forget to add sampling relevant to things that are sampling relevant.
**Liudmila Molkova** 23:49 I see, I see what.
**Josh Suereth** 23:50 So… I almost, the more I've been thinking.
Think that we should call out?
What attributes are not sampling relevant versus the other way?
So… like, on a span, I would say, here are the attributes that do not need to be available for sampling.
Because I actually think the default should be attributes are available for sampling.
**Liudmila Molkova** 24:22 Okay.
So, yeah.
ideally, either of those would be done on a span. Like, we have this identifying and descriptive attributes identity, we would have, Non-assembling relevant attributes and spense.
But this, this is hard to implement.
So, one thing you mentioned that solves this problem.
the template span, right? So there is a span, and you essentially say, okay, now the… there is a template SQL span, my, MySQL Fills in this template.
It's essentially SpanRef, right?
We need this… like, the template can also be useful. Like, SQL for the abstract SQL database for a GDBC driver and whatnot, it's also a concrete implementation.
And, my specific database can be, can reference it, so… maybe we can… we can solve it with the span ref, but in the future, it's the feature for both V1 and V2.
I don't feel we can implement it right now.
**Josh Suereth** 25:46 That's fair, that's fair.
So, hold on, I was trying to show, like, I think the difference is… the other thing is, I'm not happy with calling it sampling relevant, although that is kind of what it is, because I think in practice, the way… the way… To Jurassi's question, if I add attributes in this fashion, they cannot be used in sampling.
And so when we say sampling relevant, what we're trying to do is actually have a requirement that attributes are passed when you call start span.
To make sure that, you know, the attributes you need to do sampling are available at the right time. Which would be, start as current span child. I believe you can pass attributes here in Python. We could look at another example.
**Juraci Paixão Kröhling** 26:40 Yeah, in Go, you can, you can do it, With a kind of builder pattern, when you start to expand, like, trace with attributes and things like that.
I… I… for some reason, I never saw that, like, that… that term, like… and I was just looking, is it something new that I… that I missed for the past 6 months? And it's not, like, it's… No, that's 0, 0.
**Josh Suereth** 27:04 For a couple years, yeah.
**Juraci Paixão Kröhling** 27:05 Yeah.
**Josh Suereth** 27:06 You had to look in Semantic Convention's markdown before.
**Juraci Paixão Kröhling** 27:11 Yeah. Yeah, I just found it here in this pack, so in this pack, I think it is OTAP006, or something like that, so really old.
I guess I'm just more used to sampling at the collector side, which you can… where you can sample by anything that you want, right?
But anyway, Forget me. Move on.
**Liudmila Molkova** 27:31 No, no, no, thank you.
**Josh Suereth** 27:32 That's actually… that's actually one of the reasons I don't like using sampling relevant, because tail sampling, all the attributes are available. This is actually about head sampling relevant, specifically.
**Juraci Paixão Kröhling** 27:44 Even then, sorry to cut you, Josh, again, but even then, Perhaps we… I don't know if it is important, to talk to the sixth sampling, because they have, this whole idea about the new probabilistic sampling that I think they only take the trace idea into consideration. So perhaps naming shows here, again, as a, as a, like, the difficult part of the concept. But yeah, anyway.
I don't have a… I don't have a better name for that. I think I understand now what it is, but I don't have a better name.
**Josh Suereth** 28:29 yes. But, I mean, effectively.
Sampling decisions… so, the way the OTEP was written for sampling, it reads… oh, I can share this. Sampling decisions are made within the start spin… oh my god.
**Juraci Paixão Kröhling** 28:43 Yeah. Sorry, that's the one that I had in mind is.
**Josh Suereth** 28:46 Sampling decisions are made within the start span operation after attributes relevant to the span have been added to the span start operation, but before a concrete span object exists.
That way you can do a no-op span and have, basically have the efficient version of a span in your solution to reduce runtime overhead. So if I wanted to look at, you know, attributes and say, cool, this span is coming from internal traffic or something, I can use that attribute to just disable sampling at that granularity.
But the key thing here, I think, is start-span operation, right? So, like.
The real distinguishment feature is not necessarily that it's sampling relevant, it's that these attributes must be provided in start span.
**Liudmila Molkova** 29:37 Yep.
And effectively, when we run their markdown, we erase sampling relevant, and we're saying these attributes must be provided at start time. That's all it means.
**Josh Suereth** 29:49 Yeah.
So, yeah, but that's kind of why my… My thinking here, too, is if we were gonna do CodeGen, right? The reason sampling relevant matters, too, is when we have CodeGen, if we're gonna provide code gen for a span, we need to allow for attributes to be added to a span after the fact, but for sampling relevant, or start spin.
attributes. We need to make sure they're all provided at the start.
So we would actually do CodeGen differently based on it. So, I actually… and Lyudmila, tell me if you hate this, I like… I like the idea of public and internal.
What if the entire group is outlined as something that is start? So that when we do CodeGen, it's like, okay, here's a bundle of attributes that come in the start, here's a bundle of attributes that come later.
Because we might be doing code gen on these things, right?
especially if an attribute group is public. There'd be, like, there might be a structure that represents the five attributes together that you'd pass in.
**Liudmila Molkova** 30:59 Wait, so there is a public attribute group.
**Josh Suereth** 31:01 Yeah.
**Liudmila Molkova** 31:02 And because you can use this public attribute group on spans, it might have sampling.
Whatever. Provided the start time attributes.
And this group just exists there. In case somebody references it on Spence, it already provides information on how to use it on Spence.
**Josh Suereth** 31:23 Right, but what I'm suggesting is, I think if I make a public attribute group, I would never have some of the attributes sampling relevant and some not, because I'm providing them all as a group.
**Liudmila Molkova** 31:34 Well, it… it's… I don't know how it's going to work. So, let's… Huh?
**Josh Suereth** 31:43 Let me… let me mention the… so anything that's public, like, anything that we document public, I think there's two reasons it would be public, right? One is, it shows up in OTLP. Like, spans are in OTLP. Metrics are in OTLP. Attribute defin- like, literal, literal attributes are def… in OTLP.
The other reason we would have it public and part of our thing is because it's interacted with in code generation or documentation generation.
So, what would a public attribute group be? A public attribute group is a group of attributes that I can write a method that fills out all the attributes at once, and pass them as a bundle in CodeGen, right?
when would I… Want that group to have some things be sampled and some things not.
it feels like, at that point, I… for… specifically for public attribute groups, right, I would actually end up with two… Two things.
**Liudmila Molkova** 32:45 Okay, so it… you might want them. So if there is a thing, and this thing can… like, some information is available at start, and some is not, like, it contains the request parameters and the response parameters, and what you're saying will essentially force Someone who creates these groups to, to create multiple of them. You cannot have one.
Which makes sense.
**Josh Suereth** 33:13 Yeah, so strawman would be, I would have, you know, groups, let's say… I don't know if we're using ID for these or not, I forget what the proposal was, but HTTP, you know, server, start spin.
Oh, it has a dash, everyone's gonna hate that.
Something like that, right?
And then, under attributes, it would have… ref, whatever. And then inside of the spend.
Oh, I should make sure… we're getting rid of group, so it'll be attribute groups.
**Liudmila Molkova** 33:49 Okay.
**Josh Suereth** 33:50 Inside of the span, we would have, ID, you know, http.server, band.
It's not ID, it's type, right? That's what we named it.
Yeah, and then I could have attributes. I also want to be more aggressive with this. So, I really liked when you had ref group.
but… I'm not sold on this, I'm just writing preferences, and we can change as we go, but here we would have sampling Relevant, true.
So the whole group gets pulled in as sampling relevant.
**Liudmila Molkova** 34:33 see.
**Josh Suereth** 34:35 And every ref on Span requires sampling relevant to be filled out with true or false.
So if I ref an individual attribute here, Right?
I also need to have sampling relevant.
Just so we guarantee that a decision is made on spends.
And then… I'd also like to reduce boilerplate, I would also have template spans if necessary, but that's… Anyway.
**Liudmila Molkova** 35:08 So here, we would have a property sampling relevant as a property of The group of the group ref.
**Josh Suereth** 35:18 Yep.
**Liudmila Molkova** 35:20 And… or Attribute Truff.
Either way.
**Josh Suereth** 35:24 Yes.
**Liudmila Molkova** 35:25 We fail, if it's used.
On something that's not spense.
**Josh Suereth** 35:33 if… if this were put on… so, yeah, if I… if I were to have a metric.
Oh, wait, I gotta do the Shift-Enter. If I were to have metrics, right?
I need to stop saying right. HTTP server… duration, I don't know.
I guess it should be request duration, but anyway, we have attributes.
And inside of here, we could have ref group of HTTP server start span.
The attributes, and that'd be fine.
You know, maybe we would name it differently, but… This would be fine. This would not expect sampling relevant to be provided.
**Liudmila Molkova** 36:11 Right, and if it happened to be provided within this group, Then we would fail.
As well.
**Josh Suereth** 36:18 I don't think we should… so if you're saying if there's an attribute inside of… what I'm suggesting in my straw man is you cannot provide sampling relevant until you get to a span.
signal.
**Liudmila Molkova** 36:30 Oh, so when you… the groups themselves do not… the ref… attribute ref within the group doesn't have something relevant.
**Josh Suereth** 36:40 This would not have seemed relevant, yeah.
And the reason why I'm suggesting this is this would allow me to force sampling decisions on span and not impact anyone else.
to your other point of if someone defines sampling relevant in a group, and I reuse it in metrics, I just ignore the sampling relevant.
It doesn't matter to metric. There's no such thing.
**Liudmila Molkova** 37:07 Well, I think it's important whether we allow it or not in groups, and yep. The only reason the… the implementation is much, much easier, right, if you allow, but that's the only benefit.
So…
**Josh Suereth** 37:23 Do you mean the implementation in Weaver? I actually.
**Liudmila Molkova** 37:27 Yeah.
**Josh Suereth** 37:27 No, I think it's… it's not. From what… from what I was working on before.
**Liudmila Molkova** 37:33 Okay. I think… I think it's… they're, they're both…
**Josh Suereth** 37:36 So, so either we have to have sampling relevant that's an optional, that is not filled out for 90% of things, and then suddenly shows up in span, or we have, like, specific span reps where we can track sampling relevant, and actually fail if it's not provided. The second is easier to do, like, validation and mechanisms, because it's baked into the model.
Right .
**Liudmila Molkova** 38:00 Okay, yeah, so let's, let's try this. It would force us to write our groups in a different way, but that's, that's fine.
**Josh Suereth** 38:09 I… that's why I think the main downside to my straw man here, right? Again, I have these two goals.
And I'm focused on the Weaver implementation more than I am on the implementation of Semcov, writing all these groups. I think this makes writing the groups a little bit more painful. Possibly a lot more painful, which is why I think it needs… I wanted to fully prototype it and didn't have time, and I wanted to actually go through Semcov and see what this would look like if we split out the groups, because I think it could be really ugly.
in that. That's the downside, right? And so that's the thing I think we have to evaluate, of how much friction does it actually create on defining attributes, because you know, I will have metrics that might have two groups. I might have, HTTP… Server duration might use all the span attributes.
**Liudmila Molkova** 39:01 Right?
**Josh Suereth** 39:02 Or it could be that there are low… cardinality attributes.
So I would use the start span attributes, the low cardinality attributes, and then the span would have start span, low cardinality, and high cardinality, right? It might be that that's a convention we end up using.
That might be really annoying to deal with in practice. It might be good, I'm not certain, but I… this is what I wanted to explore. The only thing… the only reason I prefer this better is this… this restriction, right?
because you have to, like, you would have to apply sampling relevant to spans, it's forcing everyone on spans to make a decision.
**Liudmila Molkova** 39:44 Would you make it required?
**Josh Suereth** 39:46 Yes, you have.
**Liudmila Molkova** 39:47 relevant.
**Josh Suereth** 39:48 Fucks, yeah.
**Liudmila Molkova** 39:49 And you would… okay.
**Josh Suereth** 39:51 Every single ref on a span has to provide a true or false value, so you have to make a decision.
That's the only reason I like this better, is because it's forcing people to make the decisions that we think matter, for defining the signal.
**Liudmila Molkova** 40:07 Okay, let me… first think about it and probably play with it. I'll… I can repurpose my prototype to try this out. I think there is… there is an eye, I like it, is that, first, there is a… I think very high correlation between attributes that are sampling relevant and those that we include in metrics.
**Josh Suereth** 40:30 Yes.
**Liudmila Molkova** 40:30 Probably all that are sampling relevant will usually include in metrics.
And, it creates some structure that I like, for reasons I don't completely understand. So.
**Josh Suereth** 40:46 Hopefully next week, you can tell us those reasons, and we'll, we'll write them down, yeah. Yeah.
Cool.
And I do… the other thing I want to talk about when it comes to internal and external, and, like, mix-in versus not mix-in, the thing I want us to focus on is, with that discussion.
When I have two ref groups, okay.
is how do I deal with… the attributes from those two ref groups, and possible diamond inheritance hell.
What I want to have as just a trivial thing is we have very simple rules. The first ref group wins.
Challenges?
Okay? So if there's… if I inherit the same attribute name from two ref groups, the first one wins, or the last one wins, I don't care. One of them has to win.
And I understand how to flatten those out.
**Liudmila Molkova** 41:44 We don't… do we need it? Like, we…
**Josh Suereth** 41:47 We could, we could prevent an error, yeah.
**Liudmila Molkova** 41:49 Yeah, so my current idea is let's just prevent it, let's fail. If we see benefit in the future, let's figure it out, but I like that it creates very clear groups.
So what we have today is this inheritance stuff, and we tend to define and redefine attributes, and it gets lost what's defined where.
So if you define attribute, like, the specific… when you define attribute refinement somewhere.
**Josh Suereth** 42:18 It's clear where.
I… okay, then… then I… that makes me way more comfortable with the notion of a mix-in. The problem I have with mix-in is the problem I have with… designing a compiler that handles inheritance. When you start dealing with Deadly Diamond.
you have to make decisions about linearizing, like, the inheritance hierarchy and where you pull things. That is the worst code that you will maintain in a compiler.
It's hard. It's really easy to get it all, you know, mucked up, and we would be doing that. So, if we can have a clear linearization story, or prevent linearization.
everything's gravy.
**Liudmila Molkova** 43:00 "… the… the only… The reason I was suggesting mixes is the naming, because these two things are effectively different.
Internal group is ID and attributes. External group is ID, brief, stability, deprecation, attributes, and maybe something else in the future.
Yeah.
**Josh Suereth** 43:27 Yeah, thanks, Jurassi.
Yeah, yeah, I, I agree. We need a name for it.
So, let's pick a name that gives the right impression for how it's used.
And also doesn't give you a false impression of features that we never want to build.
Okay. So, yeah, like, calling it an attribute group, I think, is totally generic and awesome. Having a notion of a private attribute, like, literally, if we just call it private underscore attribute underscore group.
I honestly feel that's slightly better than Mixin, just because Mixin has a connotation of object orientation to it, that… We might not fulfill.
**Liudmila Molkova** 44:12 Okay. Okay, so… I'll… in my current prototype, I didn't publish it yet, they have just attribute groups with visibility flag. I'm not married to this approach, I'm happy to rename it and split it into two. I would focus on the sampling relevant story for the next, week.
And I might not be able to make the next week work.
I might not be able to join next week.
But I'll focus on sampling relevant, and I'm super happy with either resolution we come up with, the public versus internal.
**Josh Suereth** 44:47 Honestly, having it as a flag on the group, I'm fine with, too. Like, it's because the name attribute group, I think, clearly signifies what's going on.
**Liudmila Molkova** 44:55 Yeah, that's the main reason I like it. It's… people are familiar with it, and it clearly explains what it is.
**Josh Suereth** 45:03 Yep.
Cool.
Should we move on to live check? This one, I didn't add this to consider for next release. I actually think… I'm gonna put it on to consider for next release, and let's talk through it.
**Liudmila Molkova** 45:15 Yeah, let's talk through it. I don't know if I need to include it. The reason I'm bringing it up, that, Jeremy sent my talk, was accepted for the observability Day, and we're presenting LifeCheck, there.
And I was playing with it, and I wanted to use this time to also discuss with Jeremy and others on how we see the report for this.
showing up. So this is one of the pull requests I want us to consider, but the bigger story I'm thinking about it as linter, right? So when you run linter, it shows you lines. You violated here, you violated there.
With a caveat that, okay, there are maybe 1 million spends coming during the life check, and I don't want to get the linter for every occurrence. So ideally, what I would have is, okay, this attribute, just giving an example.
This required attribute was not available on that… on… on… If we had the notion of span identity on the span, 500 times.
Something like this.
it's… it doesn't seem like what… it's what LifeCheck does today, and I wanted to hear, from Jeremy and others how you folks think about it.
**Jeremy Blythe** 46:51 So I think the current design Is… that you wouldn't necessarily have Like, a million things coming in, because it was designed over… that you would have it, you know, in your CICD, in your test loop.
And so, you know that you're going to have a limited set of things, and you're comparing it against your model, and that kind of… that kind of thing.
to…
**Liudmila Molkova** 47:23 Even if I have 50, right? Much, oh, 10.
**Jeremy Blythe** 47:28 Yeah, like… I like, I mean, I like the PR, and I like the fact that, yeah, it makes sense to start, like.
for other use cases to… you know, reduce the verbosity, or, like, to, like, hone in on really what you're trying to express from a larger sample. I think that Makes sense. I don't know how… we would show lines of code. That would be, like, very cool. We'd have to make some kind of…
**Liudmila Molkova** 48:02 static analyzer or something. Anyway… Oh, no, no, not the lines of code, but more like, the experience you get from Linter. It shows you.
**Jeremy Blythe** 48:11 Right, right, right.
**Liudmila Molkova** 48:12 The list of violations, right?
if you ask it to report, like, you… it can give you bigger reports, but what we… what we use in River Life Check now is this JSON thing that lists all the different, advices, right? And some stats. So maybe part of this, or maybe we want to write it to STDR, or, like, this list of violations of what occurred in, like, compact form. So you can look into the report, but you also get the The summary of actually what was broken.
**Jeremy Blythe** 48:49 Right, yeah, the way it works at the moment is… Every single signal that comes in is converted into a sample.
The sample is compared against the semantic convention model that you provided.
And then that sample is augmented with the results of the live check, and then that's just put into the report. And so if you've got a million signals coming in, you get a report with a million samples with their results included in them. So I think what you're saying is, I'd like to see that inverted, where I'd want to go, like.
This thing happened, and maybe a count of how many times it happened.
So I could have… there was a violation on this span, on this attribute, and it happened in this live check run, it happened, like, 999,000 times.
As a… as a more succinct report. Yes.
And it's…
**Liudmila Molkova** 49:46 For… for the use case, you, We're working on the… like, specific signal, CICD.
Do you think that this… oh, that's now coming to this PR? What this PR does, it… for everybody, who is going to get a report, it sets the minimum level of advice To get in the report.
Do you think this makes sense Or… your case.
**Jeremy Blythe** 50:36 For the test loop sort of case.
**Liudmila Molkova** 50:40 Yeah.
**Jeremy Blythe** 50:44 Personally, I think I would still want to see everything. The reason I say that is… If you've got all of the data, you've got more clues as to where the problem came from.
So… so… if I'm hide… if I'm hiding the fact that, or am I… So if you're… you're just going to hide… an informational… Advice.
What about things that don't have any advice at all?
Are we still gonna throw those?
**Liudmila Molkova** 51:26 No advice at all?
Do we write them in the report?
I think Josh has a question.
**Josh Suereth** 51:34 Yeah, I'm just thinking about this, like, I… I see this feature kind of like, test suite coverage?
and code coverage. Like, a little bit between the two.
So, when you run a test suite, like, the report you get on the command line might be, trimmed down, and then there might be, like, a full dump somewhere of the test suite, of, like, here's all…
**Liudmila Molkova** 52:02 Oops, is it just me?
**Jeremy Blythe** 52:04 No, Josh just exploded.
Interesting, yes. And I guess his camera and mic broke.
Because he's still connected.
Oh, no.
**Liudmila Molkova** 52:22 You might… no, he's not.
**Jeremy Blythe** 52:24 Now we've got pictures.
Your pictures are back, Josh, but no sound yet.
Complete us. Complete disconnect.
I believe at the moment, in the report.
It will print… it will print out the… and say there's an attribute, and it's perfectly fine. It's just like, this was an attribute with the value you gave it, and… It's all good. It's green.
Nothing wrong with that.
And so, if you're hunting… if you're searching through your report to try to find what was going on, you would… you would have that information still in the report.
So you go, like, oh, this is where I put that attribute with that value in. Search. Oh, that's that test.
**Liudmila Molkova** 53:23 So this is in samples, right?
Can I, can I share? Hold on, so… There are two flavors of the report, right? One is, what you get in STDL, the other one, what I'm playing with, is JSON.
report.
Can you see my screen, by the way?
**Jeremy Blythe** 53:46 Yep.
**Liudmila Molkova** 53:47 Yeah, awesome.
So, there were the samples, right?
Oh, okay. And then somewhere there are devices.
Okay, so here. There is an improvement advice.
It's like, if I'm just… it's the flow you… you're… in your mind, that once I get Exit code that's not zero.
I open some sort of a report, capture this TD out, or this thing, if I… configured it, and I look for violations, right?
And then, from here, It's attached to a specific sample.
And then… Since we captured all the information for the sample, I can kind of understand what was Wrong deer.
This is the flow.
**Jeremy Blythe** 54:53 Yeah, we… I guess it just helps.
In that flow, right?
**Liudmila Molkova** 55:01 Okay, so maybe instead of working on the… so the proposal I have is to just not return this, to make this report more compact, but maybe I should be… what I'm really after.
is, additional STD out that would say, okay, this advice type with this level happened.
For this attribute X number of times.
And then you can use it for the quick assessment of what was wrong.
**Jeremy Blythe** 55:39 Yeah, and if you… if you go to the bottom, there's the stats section. I feel like that could be in the stats section.
**Liudmila Molkova** 55:45 Mmm…
**Jeremy Blythe** 55:46 Though I kind of call out… So I do call out, like, how many violations there were, how many…
**Liudmila Molkova** 55:54 How many? Yes, but, the.
**Jeremy Blythe** 55:56 That could be… yeah, that could be improved in that section of the report.
**Liudmila Molkova** 56:01 Nice, okay, yeah.
**Jeremy Blythe** 56:02 I'm saying it could all be in the same report.
**Liudmila Molkova** 56:07 What I'd like to see, like, when I run it, right, that it prints the summary.
That it's actually… well, for me, it would be extremely hard, if I get a failure in the CI, to look through this report and filter viola… I would only care about violations, honestly. Like, I was thinking about implementing this for, let's say.
up in telemetry instrumentations, part of their CI check, right? That they are compliant with semantic conventions. And then having, like, two lines of the report, of the outcome.
when you look into CI logs is much more approachable than downloading this report and actually Filtering through it.
Okay, let me try.
**Jeremy Blythe** 56:59 My department.
**Liudmila Molkova** 57:00 stupid. If we like it, we like it. If we don't, I don't mind at all.
**Jeremy Blythe** 57:06 Yeah, I think that makes sense.
No.
**Liudmila Molkova** 57:15 Yeah, because…
**Jeremy Blythe** 57:15 It is a lot. But I… you know, you can… you can… you can have the… what we call the ANSI format.
you can have that as the report, you know. You can choose whether you want JSON or that one. It isn't.
**Liudmila Molkova** 57:31 Yeah, it's still very verbose, right?
**Jeremy Blythe** 57:34 Yeah, oh yeah, and any of the… but I'm just saying, any of the types can go to any of the outputs, so you can have… this on standard out, or you can put it to a file, and likewise with the other one.
**Liudmila Molkova** 57:46 Yeah, comparing it to, not Winter, but the compiler, you can get a very detailed information about your build process, and then at the end, you will have a list of errors. So, and that's what I'm after.
**Jeremy Blythe** 57:59 Yeah, no, that makes sense. It'd be interesting to see it from… I, like, these other points of view, other use cases. But, you know, it was just… It was really built around I've got this small model, how do I check that I'm… that's why there's that coverage thing that we were talking about in Slack as well, I think.
That there's a coverage which doesn't make sense when you've got, you know, the entire semantic convention library.
Because, you know.
Or maybe it would, I don't know, but not normally.
**Liudmila Molkova** 58:35 that we…
**Jeremy Blythe** 58:36 Anything from that perspective? Anyway, yeah.
**Liudmila Molkova** 58:40 we have less than one minute left before we part our ways. This is actual, just out the instrumentation Python, and found 2012 violations.
**Jeremy Blythe** 58:48 For a few instrumentations that I run, so it's extremely useful.
Yeah.
Yeah, that'd be great to see your ideas for the report, 100%, yeah.
**Liudmila Molkova** 59:01 Awesome, thank you.
**Jeremy Blythe** 59:04 Bye.
