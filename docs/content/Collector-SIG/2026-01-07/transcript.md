SIG: Collector SIG
Date: 2026-01-07
Duration: 94 minutes
Zoom Recording URL: https://zoom.us/rec/share/ccVIb8Zrixlqh-RNtn_knUfJxuWEl1Q5L77V2QkTzMOUK9ZRcYcYFgP583qX_TTp.LWsMlBSUv4_XU_Dh
============================================================

## Zoom Recording Transcript

**ploffay** 05:56 My mouse is tricking me.
**Evan Bradley** 06:14 Alright, we're sitting at, 5 minutes past the hour here, should we get started?
**Jade Guiton** 06:23 Yeah.
**Evan Bradley** 06:24 Cool. Does anybody want to go through the… Stability issues on the board?
I mean, I guess, does anybody have any stability-related discussions they would like to… bring to the table here Okay, that was an extended enough silence, I'm gonna take that as a no.
We can feel free to come back to, that agenda item, if somebody has something later, or… if… I think Pablo and Jod, you've run that item before. If there's something you would like to review specifically there, let me know. Otherwise, I will continue on with my agenda item.
Cool. Sounds good. Cool.
So, we're, the OTL code owners are, reviewing a PR right now that provides access to the, Golang context.context object inside of OTL, and we're trying to figure out how we want to name the path.
So, we have a couple of options available for this. It's mostly a matter of what we think is going to be a, is going to be maintainable going forward for us as OTTL maintainers, for adding, you know, new paths, alongside this. Right now.
So the context.contacts, you're going to be getting, you know, certain objects out of the path there. Right now, we have the, collector, the client library that we pulled these out of, so a couple of receivers will put things Into the context, using that key. So it's a lot of, like, request metadata and things like that. But in the future, there could be additional, pieces of metadata here.
So we're trying to figure out what makes sense in terms of a path that tries to explain this to users that may not be familiar with Go's, context passing, in depth, but also gives them an idea of what, what kind of information this path is going to provide. One thing that we're considering is scoping, making a new hotel call path, and then scoping this under that so that it's, Very explicit that this information is obtained from the collector and not necessarily from within the payload.
So this would apply currently to context.context, but in the future could… you know, hypothetically, like, extensions or any other sources of data, that we would want to pull from. It would make it easy to add it all under this path. However, it would make the path longer.
We could also do something like request or client. So these would, you know, this would have us make new pads for, any additional information we would want to add, pulling from context.context or otherwise.
It would make the path a bit shorter, but would also mean that, you know, you do lose that… some of the benefits of that namespacing.
Just a little bit of extra, context, forgive the pun. We don't want to use the term context, because it's such an overloaded term, so we've tried to opt not to refer to it directly like that, even though right now we're just pulling from the context.context object.
this is… I'm just… I want to make a call to the… the community here, just to see if anybody has any strong preferences for, how you might like to see this named, or if you have any users with OTTL experience, what you think that they would find the most obvious. Our goal is hopefully that you can read the path and intuit what the source of the information that you're reading is, to the best of our abilities. Obviously, docs are going to patch any holes there.
But that's the… the overall question. I'll open the floor now in case anyone has any thoughts or questions or comments.
**Jade Guiton** 11:18 My personal vote would be client, because that's what the struct is called, and also the module that defines it.
I'm curious what the benefits you mentioned would be of namespacing all context-related data under one namespace.
**Evan Bradley** 11:38 Sure. So, I think my argument against I don't mind the name client, but the reason that I don't want to derive it from the Go module name is that OTTL users aren't going to be necessarily familiar with the collector internals, and so I… I want to make sure that the name makes sense independently.
And that we're… that you can, as an OTCL user with no knowledge of the collector, go to a statement and understand To the best of your ability, what client means. The reason that I like hotel call is… It, it groups all, like, non… not all.
But, because we have the cache, right? We have that cache path that is the temporary map that, you know, persists throughout the statement execution. But, the reason I like hotel call is because it makes it… I think it's a fairly well-known abbreviation for the collector, and it makes it obvious that this comes from… data that exists somewhere inside of the collector and not, data that is passing through the collector, if that makes sense. The goal here is that we want to make it obvious to users that this is additional metadata that is available on top of a request and doesn't come from the request itself. I wouldn't want to… I don't want to confuse users and think… and have them think that they're accessing data within the payload.
That's mainly the reason for hotel call. So we could put not just, request context, but we could put, any other thing that might be in the context.context object under… it would be hotel call.
I don't even know, like, you know, retry information… I'm making something up, that probably isn't a good example. The best example I can come up with is extensions. So let's say you have an OTL processor, or an OTL-enabled processor.
that uses an extension to get some kind of metadata from a, an outside system. You could say otelcall.
I'm trying to even think here, you know.redis, and then your keys, or whatever, if you're… let's say you're reading from a Redis store.
Again, I'm struggling to come up with a good example on the spot, but the goal here is that you'd be aware that, okay, this is coming from the collector, and then the collector is reading from a Redis store. That's kind of what you could get out of that path. The big thing is that we don't have IntelliSense or anything else, like, you're… if you're reading a statement that somebody else has written, there's no… there's no good way… I mean, you're just essentially reading statements in a YAML file, so the more… The more context that we can provide.
within a given statement, I think the better. We generally try to… tend, within reason, to be more verbose in OTTL.
**Jade Guiton** 14:32 Hmm, that makes sense.
I'm not a huge fan of hotel call, like, as you say, it is a well-known abbreviation, but, like.
The data isn't necessarily specific.
to the collector, doesn't really come from the collector. What about something, like, external, or extern?
**Evan Bradley** 14:53 Okay, I think that's… that's a… that's a good one to add to the list.
**Jade Guiton** 14:58 Okay, it would make it a bit clearer, at least to me, obviously, it's very subjective, but it would make it clearer to me that this is not from the payload, it's an external piece of data.
**Evan Bradley** 15:10 Okay, I think, I mean, I don't want to commit to anything on the call here, but that's a good… I appreciate that feedback. I think that we'll… we'll play around with a couple of those names and see if anything sounds good.
And then we can… if you're interested, I'll, I'll ping you on the PR as well.
**Jade Guiton** 15:28 Sure. I don't have a very strong opinion, but yeah, I think overall.
people are not going to understand what client or any of those mean without looking up the docs anyway. It's a relatively niche feature.
Oh, that's true I think even among component developers, so… Yeah.
**Evan Bradley** 15:49 So, the target for these paths is going to be end users. We're going to be providing this within… the OTTL, like, standard context, so this would be available to any user using a component that uses OTTL and has one of these contacts in it.
**Jade Guiton** 16:09 Right, yeah. I guess this would probably be the first exposure of most people to the concept, that we keep around information from the receiver side.
**Evan Bradley** 16:19 Right. And that's… that's… I mean, I… like you said, I think that… the, it's gonna be necessary to read the documentation to really understand it at the end of the day. But the closer we can get people to having some level of intuition about what a statement does, even if they're just reading it.
or doing minor edits on it, I think, it will… it'll improve the overall user experience.
**Jade Guiton** 16:46 So that's where I would see something like external coming into play.
Yeah, I think that makes sense.
**Evan Bradley** 16:57 Edmo, anything that you would want to add?
**Edmo Vamerlatti** 17:02 Yeah, not really, you know, naming is hard.
**Evan Bradley** 17:06 I was struggling with this for a while, but the main goal, as you explained it, would be to find the prefix for this.
**Edmo Vamerlatti** 17:13 So we could expose the client, but again, client, it's a very common path, so maybe other context, we have the field later, and that would be a problem, that's why you need that path as well, that prefix for the context path.
And they… and yeah, wow.
I don't know how big it's gonna be, but we need to think about it. Otherwise, we're gonna end up exposing data inside this path. With the graphic, it doesn't make sense at all.
That's why we need to… To consider all the options we have right now.
**Evan Bradley** 17:45 Cool.
Okay, alright, well, if anybody else has, ideas, we'd welcome your input. The goal is that we should… we're just looking to make this as accessible as possible to as many OTL users as possible, so any ideas are welcome.
I also have the next agenda item, and I see, David, that you've added some information here, which I really appreciate.
I…
**David Ashpole (dashpole)** 18:21 I'm just gonna scan this real quick… Okay, so, that all makes sense to me. I guess my question is, is there a way that… my concern is, from what I understand, and you can correct me on this.
**Evan Bradley** 18:38 If I am… scraping with the Prometheus receiver, and I want to use Delta metrics, which.
**David Ashpole (dashpole)** 18:45 from my quick survey of most vendors, and my, explanations from my team, are really the most efficient way to collect metrics. Cumulative is mostly just, from what I understand, a compatibility, kind of feature that we have to mostly, I think, support Prometheus. So, if I want to create a pipeline, with the Prometheus receiver in it, I will automatically need to add the receiver, all that config, and then the start time processor and the cumulative delta processor, just to get working metrics in the collector.
So, I guess my ask is, is there…
**Evan Bradley** 19:24 Any plans or ways that we could.
**David Ashpole (dashpole)** 19:27 I mean, it's not complicated, right? Because both the processors you can just include in a pipeline without any config. It's not like it's particularly tedious.
**Evan Bradley** 19:35 I guess just from a UX perspective, it seems not necessarily ideal that you need to almost always include two processors when using the Prometheus receiver.
**David Ashpole (dashpole)** 19:45 Yeah, I mean, we had considered making the… Metric start time processor, a receiver helper.
But I don't remember the exact details. I think… There wasn't, like.
People didn't feel that it was necessarily that much cleaner, and it is… It… Yeah, it is nice to not have it in the Prometheus receiver, because a lot of people who are using it.
or who were using it had to turn it off, or have a big performance penalty, because it is doing… it is stateful. There are some nice properties. I understand that you have to set two processors. I hope that's not… Yeah, I think right now we're in the best of kind of an ugly situation, but the nice thing is that over time, we hope to introduce start times proper in Prometheus, and so I think that's where we're trying to head.
**Evan Bradley** 20:46 Okay.
**David Ashpole (dashpole)** 20:48 Alright, no, that makes sense to me. We just, internally, we got bit a little bit by the, the feature gate transition that disabled the, the thing, and it kinda… I guess it just made me go back and ask, but if…
**Evan Bradley** 21:00 there is… if that's the long-term solution, then I can, just bring that back, and I think that it will be… That will be adequate.
**David Ashpole (dashpole)** 21:09 Yep, I mean, the metric start time processor is a drop-in replacement for all the .
**Evan Bradley** 21:15 prior behavior.
**David Ashpole (dashpole)** 21:16 Right. It's… Once you figure out… yeah.
**Evan Bradley** 21:19 Yeah, well, it's mostly just the fact that, let's say I'm using an older version of the collector, I have that functionality in there, you know, that past a certain point will, you know, suddenly my metrics stop working. Like you said, it's drop-in, it's easy to configure, all that, It was mostly just a question of, like, something like the receiver helper, Or along those lines, but if it's a temporary situation, I think that's easier to live with.
Of course, I know, I don't know what the timeline is on that, but, still.
**David Ashpole (dashpole)** 21:49 switching to new protocols is, I suppose, temporary, but it might be a few years, you know?
**Evan Bradley** 21:54 Right.
Well, okay, I guess if it's a few year… okay, I was thinking on the course of a year. If it would be a few years, is there… Do you have… would you be able to link me to the discussion on the receiver helper? I'd be happy to… I mean, there's other solutions to this, you know, we've talked about doing, what is it, some kind of, like, config templating before, you know, where you'd say, like, Prometheus receiver with delta metrics or whatever, and it just, you know, would instantiate that in your config. But I'm just trying to think of something that's kind of a one… A one and done for users.
**David Ashpole (dashpole)** 22:31 Yeah, right. It would be interesting if, if, like, cumulative to delta and delta to cumulative were also, I'd actually… the other way you could think about this is actually thinking of it as potentially being part of the exporter helper, because some… Like, not all exporters care about start times, so if it was, like, a thing that came with your receiver, you might only want to use this if it was going to a particular exporter.
Let me find the original… I'll link it. Is there any… are there any other questions, that we should discuss live on the call?
**Evan Bradley** 23:16 Nope, really appreciate all the context there.
Okay, Tiffany.
**Tiffany Hrabusa** 23:23 The floor is yours. Thank you. Happy New Year, everyone. I am here to give you an update about the collector docs refactoring. Phase 1 is nearly finished. There are, three PRs that just need, a few small tweaks, and then they'll get merged.
So, I am about to begin Phase 2, which involves creating a bunch of new issues. And, I've linked the project description and the project board.
The project board is pretty empty right now because I have not created the Phase 2 issues, for good reason.
But what I'm here mostly to do is ask for, anyone who would like to volunteer to help me, work on Phase 2.
Phase 1 was kind of the easy part, it was mostly just copy editing and moving some pages around.
Phase 2 involves creating new content, to fit in with the new architecture that we, we've settled on.
And… I can create some of that content myself, but it would be really great if I had a subject matter expert who would, kind of pair with me on that.
And if no one has the time, capacity, or willingness to actually pair with me, then, I would need some… some people to review these PRs. So, if anyone wants to speak up now.
That would be great. If you have any questions about what that involves, the project description probably will tell you what you need to know, but I'm happy to answer them.
**Jade Guiton** 25:04 Are a lot of these… are those pages brand new content, or mostly… Restructuring of existing content, because it seems like… It seems like a lot of those are more or less already covered, but I guess we're… Changing the way it's organized?
**Tiffany Hrabusa** 25:26 So… in… in the Phase 2, I don't know if I can link… yeah, I guess I can, actually.
I'll put it in the chat here.
The Phase 2 kind of breaks down what I see being accomplished in this section. There is… a lot of what happened in Phase 1, which was copy editing and moving things around, but we need to create, a new page as an introduction, we need to create a page, what is the collector? Because we don't really explain that very well from, like, a new user perspective.
We don't have a very good explanation of how to choose a distribution based on your own needs. So those are… we could probably repurpose some of the content that we have in the docs, but largely, I think it's going to involve new content.
There's also, explaining the configuration file structure, which, again, we have, explanations about each of the components, but we don't really explain well how you build, the, the configuration. So… like I said, a lot of this I can… I can kind of… scaffold and kind of draw it myself, but I am far from an expert on, the internal workings of the collector, so… I would really, appreciate, anyone. And Jad, I know that you've been reviewing all of the PR, so I really appreciate you doing that. But if there's anyone else who wants to step in, and… and help out with this part, and fair warning.
Phase 3 will be even more intensive, because that's where we start doing a gap analysis.
And we figure out what is just not covered at all in the docs, or what is outdated.
I'll be using some AI tooling to help me assess that, and then we'll have to create the docs for that, too.
But right now, let's just focus on Phase 2.
So yeah, if anyone has any other questions, I'm happy, to answer them now, or you can, ping me afterwards if you, want to.
get involved.
**Jade Guiton** 27:44 Oh, yeah, for the record, yeah, I'm willing to help, write some of the pages for Phase 2.
**Tiffany Hrabusa** 27:52 Thank you, I appreciate that.
if there… if no one has anything else about the refactoring, the sec… the next item is also mine, which is just to plug Hotel Unplugged. It's an unconference that's happening in Brussels the day after Fosden.
So that would be February 2nd, and, just under a month.
There's a registration link in the meeting notes, we encourage you to attend if you can, especially if you're in Europe and can make it. If you can't attend, it would be really great to… if you could just, maybe plug it with your network, because what we're hearing is that people aren't hearing about it, even though we've been doing some promotional materials through the, OTEL accounts. It would be great if, some of the maintainers and approvers and contributors would, just mention it on your LinkedIn account or on your socials, so we can make sure that everyone who would want to attend can.
That's it for me.
Pavel?
**ploffay** 29:11 Hi, everyone. I would like to discuss the DPR I opened to improve the collector config JSON schema generation.
The… what the PR essentially does, it extends the… the metadata gen.
with a new field, under schema to kind of optionally generate JSON schema for a collector component.
And I realized there is an alternative PR opened, in the country repo.
By Jake? I'm not sure it's… his name is Jake, but I thought maybe it's a good idea to discuss it here on the meeting.
Yeah, it seems like probably the person is not here, But, yeah, I would appreciate some… some review on my PR, or maybe the… the Jacob's PR, if… I'm not sure if… It's the right name. But what is kind of controversial to me is, in the second PR in the country.
The… Point 4 mentions that The… the approach that he wants to implement is to generate a tool after we have the schema that would generate the Go configs out of schema, and I think this was discussed here.
couple meetings ago, and we kind of agreed that we want to probably keep the Go configs as the source of truth, and just generate the schema from the… from the Go, and don't go into the… The approach of, you know, generating Go code from… from, from JSON schema.
**Jade Guiton** 31:50 Yeah, I'm… yeah, I think we discussed it.
And at least, I think for… at least for the time being, it makes sense to keep the Go Config structs and generate the schema from there.
I think maybe the best option to avoid, like.
Having the word beaten Dung twice in two different ways would be to… Reach out to this person?
I don't know if they're on the Slack or not.
But, yeah, I think, yeah, there's been relatively little movement on all those PRs with the winter break.
But, but yeah, I think it would be good to coordinate.
**ploffay** 32:46 Yeah, I think from the implementation perspective, they are not, those two PRs are not… very different.
It's just the way how they are, kind of… Exposed in the repo.
That's what's different.
**Jade Guiton** 33:10 Yeah, that makes sense.
If nothing happens on the… on the PRs in, like, a week, It was the option of pinging the reviewers.
But, yeah.
I think it would be good to… avoid doing the review work and the design and implementation work twice, I guess.
**ploffay** 33:34 Yeah, absolutely. I mean, the second PR, it happened, yeah, during the, the break, and it was kind of very quickly merged, there was no chance to… to have a second look. But anyways, please take a look at the… these PRs. I will probably start a conversation in the collector channel and ping Jake, if that's his name, so we can… A bit more discussed there.
**Jade Guiton** 34:03 Oh yeah, you're right, I didn't see that there was an initial PR that already got merged.
**ploffay** 34:08 Yep.
**Jade Guiton** 34:26 I think I see there's a PR by Antoine about an RFC.
If there's multiple people wanting to implement this, maybe it would make sense to… Make sure we have an RFC so everyone agrees on the details.
Instead of keeping things in separate PRs.
**ploffay** 35:08 Okay, I guess that's everything from me. I will then, as I said, start the conversation in the… on the Slack channel, so we can… A bit more coordination there, and… mention it in the RFC from one to one.
**Jade Guiton** 35:24 Thank you.
So the next point is from Israel.
**Israel Blancas** 35:36 Yeah, hi all. So, the things that some… some weeks ago… Sean, who is one of my folks, from chronologics, came on, and while we were talking about this, component called AWS ECS Attributes Processor, right? Well, there were… there was some good conversation about, Some possible alternatives, right, about how to implement this thing or something.
And yeah, well, there was also some conversation on the… on the ticket, right? Right now, it's not… pretty clear, at least from… from our side, right? What… The people would like us to… to do, but we would like to have, like, this… Features, right, as part of the… of the implementation of the collector, so if you can take some time, to read, because the ticket is a little bit long, right? To understand the different things and, you know, post your ideas or something like that.
Yeah, even if you… if you want directly ask… ask about some extra information or something like that, we will be, like, more than… than happy to… to answer.
Yeah, it was just about that.
Thank you.
**Jade Guiton** 37:26 If no one has specific comments, about the AWS ECS attributes, the… Issue, that was the last item.
In the agenda, so… Does anyone have anything else?
To talk about?
It seems not, so, in that case… I guess, meeting adjourned. Thank you, everyone.
**Andrzej Stencel** 38:01 Thanks.
