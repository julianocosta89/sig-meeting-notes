SIG: Collector SIG
Date: 2026-04-22
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/GmON37wObEFehpRRhtO1Qgd0G-VYz7hK7qbVmZO52uluC1QP7Fw-SuMD24583r-6.BDtJxSh4c-xtdcXP
============================================================

## Zoom Recording Transcript

**Andrzej Stencel** 02:04 Hello.
**atoulme** 02:10 Hey, buddy.
I knew.
Alright, let's go. Any high-party issues we should look at?
Let's take a look.
I will be sharing my screen.
Okay, so… Overview, this is the current view of what we're trying to stabilize.
Is there anything that is burning that we need to look at in progress right now?
Let's still a work… NG, you aware of the work here?
**Andrzej Stencel** 04:12 Yes, I am.
**atoulme** 04:14 Okay, okay.
I'm not, so… Okay.
Any questions, anything we should review here in particular?
**Pablo Baeyens** 04:30 There's been a lot of progress on the Prometheus side, but it's mostly on the spec.
**atoulme** 04:35 Nice.
Is the host metric receivers, pending on system metrics, to be stable?
**Pablo Baeyens** 04:54 Yeah, the process namespace will be marked as for this candidate soon-ish, and then they have to go through system.
the system namespace. But yeah, that's mostly what… Has been… being worked on right now.
**atoulme** 05:12 Huh.
Okay.
**Pablo Baeyens** 05:22 Not much progress on research stage process or anything.
**atoulme** 05:26 Alright.
Anything people would like to discuss further?
So, if you're interested to participate in making the collector stable, this is where you go.
And these are the issues that are assigned to this.
And now I'll give the floor to Pablo. Would you like to talk about that announcement?
**Pablo Baeyens** 05:46 Yeah, sure, should be quick, so I guess there's this post from the Bloomberg website, and I think the CNCF has also published something, but… It's the exact same blog post. Okay, well, so there's a bunch of Bloomberg employees, which… are going to be… Sorry.
participating in OpenTelemetry, some of you may be mentors, And… yeah, just if you see them around, be… be kind. They… they already know how to do software, so they have some background, but they may be new to OpenTelemetry.
And it is… I think, like, 30 people? I don't know, it's a lot of people.
**atoulme** 06:36 Oh, wow.
Okay, alright.
Gotcha, you have the next item too, please. Keep going.
**Pablo Baeyens** 06:46 Boogie, yeah, so, I've had some conversations about, how we can improve The experience for people that cannot attend this meeting, there's… especially people in APAC, because we have an APAC-friend meeting, but it has much less attendance than this one. Yeah.
And, yeah, I don't know, I was wondering if… There are things that we could do there to make it more accessible.
To them?
I brought down two ideas there, but I'm willing to… discuss anything else. One is… that we could try and post the most important updates on AutoCollector Dev.
And then, well, we could also make the meeting notes probably more useful if we… split them down. There's a bunch of topics that are, like, please review my PR, that we could group, I don't know.
I'm not going to volunteer to do the… posting the most important topics every time. I could volunteer to do that… sometimes.
So, yeah, I don't know if there's sort of ideas or other people that would be willing to help with this.
**atoulme** 08:13 Should we… should we just, when we go through the agenda, we could just say, oh, this is worth busting to Slack?
Just to reinforce.
**Pablo Baeyens** 08:24 Okay, yeah, that sounds like a good idea.
**atoulme** 08:28 I've… yeah.
**Jade Guiton** 08:31 I feel like the meeting notes… Should be… the existing meeting notes document should be enough, we just need to structure it in a way that's a bit more friendly.
And also, I guess, to note, These meetings are recorded.
So… Maybe one thing we could do is also post the link to the recording, if we have access to that.
Because there's always gonna be more information there.
**Pablo Baeyens** 08:57 Part of the point is… not necessarily that people can access the content of what we discussed here, but also, like, that we spark conversation in Slack by posting it on Slack, and we continue things on Slack.
We could post the recording link, yeah.
I think something a bit more structured would be… more amenable to… to generate discussions, but…
**Jade Guiton** 09:26 Yeah, I mean, we can do both. We can have a link for the full thing, and a link to the meeting notes, and a summary of I guess whatever we think is relevant to ping in Slack.
**atoulme** 09:39 That's fair.
**Pablo Baeyens** 09:39 Tiffany?
**atoulme** 09:41 Good.
**Tiffany Hrabusa** 09:43 I had a suggestion for, a different meeting that I attend. We use pills in the Google Doc, and there's just four selections. Decide, Action, Discuss, and then Form.
So, before you put your name in brackets, you just add the pill to your agenda item.
And then, it makes it easier to parse.
the things that are just in form, you can kind of glance over. Anything that's discussion or decide. Obviously, we'll have, or should have, greater note-taking, so that we can document what was said.
**Pablo Baeyens** 10:21 Sorry, those were the side, action, discussed, and there was a fourth one?
**Tiffany Hrabusa** 10:26 Inform.
**Pablo Baeyens** 10:27 Inform. Okay.
Yeah, I like that. I, I… I'll try and do that for today, and… We can start with that. I don't want to do any super big changes, but… That'll work for me.
**atoulme** 10:43 Yeah, maybe some small changes start there, and then we can definitely reinforce that just looking at Slack, we have 549 people on that Connect2Dev channel, and they kind of signed up to be in the spammy channel.
There's a Hotel Collector channel with 5,546 people for more support-type discussions.
So I think the calculator dev is clearly meant to have technical discussions about this or that PR, and we can probably inform, you know, push on that as much as possible.
Okay.
Alright, it looks already better. Thank you, Tiffin.
Thank you, Pablo.
Evan?
**Evan Bradley** 11:32 Yes, so I just want to broadcast this and get any feedback, if there is any. Basically, we have a top-level function that the collector calls to Basically introspect all, like, the entire collector config, go through all the config structs, and call or just do validation on them. It'll call a validate method, if there is one. There's an interface that they can implement to opt into this, or it will just go through and, just kind of quickly check.
Basically.
So, this hasn't changed in, like, a year, and there's a lot of modules that depend on a, an unstable package because of this, so, I think we should just bite the bullet and stabilize it, but I want to check just in case anybody's got some… validation issue that's been floating around in their head and isn't clearly annotated in the issue tracker. I tried to look through, our issues, didn't see anything.
But either in this call or on the poll request, let me know if… You have any concerns about this. Otherwise, I'd like to get this in and keep pushing forward.
Alright, Pablo.
**Pablo Baeyens** 12:56 Hey, it's me again. Yeah, so I… I'm very thankful that Andre and… and… Tony… Antoine, sorry, remind me and other core maintainers about ready-to-merge PRs, I would like to… I did not have to do that, so I have this PR that let me… Yeah. To just basically automate a weekly message, with a list of the PRs that are ready to merge on OpenTermetry Collector, and… the, also, the RFC starting final comment period.
Sure. I don't want to make the channel too spammy, so I wanted to check here if this is an idea that people like or not, and if you like it, if you would want to see something else on that message.
**Andrzej Stencel** 13:56 Do these Slack messages mention a new one, or…
**Pablo Baeyens** 14:02 No, so it would just be a link to… so… it would say how many PRs are ready to merge, and have a link to a query where they are all listed, but it would not mention anybody specific.
**Andrzej Stencel** 14:16 Yeah, sure.
**atoulme** 14:26 I'm all for it. I… I would just say that the only 4 people who can merge things in Collector Core.
This is for them, unfortunately, right? And, how many maintenance do we have on core?
Yeah, we have. Yeah.
So…
**Pablo Baeyens** 14:46 My hope is that we can extend this for things that are useful to more people, like, the final comment period thing, if it's too annoying for… The rest of you, then, like… Play such a.
**atoulme** 14:59 boat.
**Pablo Baeyens** 15:00 collectors.
There's a public shame element also, like, you forced me to do it.
**atoulme** 15:06 Okay.
**Andrzej Stencel** 15:08 Well, so if it's just a link to the query.
There's a number, right? Okay. Yeah, I guess.
**Pablo Baeyens** 15:22 I'll try it out and, like, put a reminder to ask you again in 3 weeks if you think it's annoying.
**Andrzej Stencel** 15:29 Makes sense. Thanks.
**atoulme** 15:46 Okay.
Next up… I think, I think so, sorry. I'm okay, you should do it, you should try it, and see if 3 months, and then see if people complain.
If it doesn't help, we stop.
Right.
Okay, let's go to Yasmin.
**yasmine** 16:13 Hi, I'm Yasmin. I'm new to the community here. I have been working on a new component called Cardinality Guardian.
And it's basically trying to remove the hardships that engineering teams are constantly having, for metric cardinality exclusions, whether blowing up the bills or, like, having, loss in the matrices, due to, like, the cardinality.
Like, existing OTL processors let you drop pictures based on, like, static rules, but I wanted something dynamic, so I used, Hyperlog++.
Data structure to statefully track active time series in real time.
And if a metric preach defined limit, it's surgically, like, try to strip the exploding attributes to collapse the series.
and saving the core metric data without the penalty. So I'm here today to get feedback and learn about the process of donating this to the OTL collector contributor, and yeah, if you have any questions.
**atoulme** 17:25 Yeah, I mentioned I was interested to sports, sorry.
**yasmine** 17:27 Yes.
**atoulme** 17:28 I do have a couple questions for you.
But, anybody else first?
Alright, so first question is, and this is very, innocent, would that work with, logs and spans and metrics, or is it just one part of your signal?
**yasmine** 17:50 So, I started with metrics first to see, like, the interest of the users of this, and, like, I have a very long roadmap, but, like, hopefully if this is something people are interested in, we can move to the next port.
**atoulme** 18:09 You have a longer map? Okay.
Okay, that's good. Okay, yeah, I mean… this type of clever algorithms that allow us to do this type of sampling, or be good about calculated explosion is great.
And do you have any metrics or anything like that that's being, That are being captured at our internal metrics to this particular processor.
**yasmine** 18:40 So I did, like, benchmarks, and I also did, like, the Docker Compose to do, like, the… more of, like, a 5-minute test using the telemetry generation, like, matrices. I'm not sure if this is answering your question.
**atoulme** 18:55 I'm looking at your metadata YAML file, right? So you have process coordinity labels tripped, estimated, offenders, active.
and rejected. And so, for example, you… I think that would be great to alert on for someone in some ops positions to say, oh, okay, I see that we're dropping some dimensions from our metrics because we're above a certain validity. So, that's good, that's helpful for me.
And that's mostly the question I had, is like, do we have any way to… to track the effect of that processor?
Do you also annotate the data point itself when you touch it, or you just let go?
**yasmine** 19:37 So, there's two ways today. So, there's the tag-only way, so basically, your data is kept as it is. You just get, like, the tag-only if set true to know which, labels or attributes are offending rape labels. So, without cutting anything. And then, if you decide to go with the tag-only to turn it on, the, the guard, like, the processor to be turned on at that At that point, you can get from… there is a metric that will tell you Which exactly labels our, the offenders, that has been cut.
**atoulme** 20:13 Understood. Is this reminiscent to the other processor we had recently at it, folks?
**Mikołaj Świątek** 20:22 You mean the one… the one which tries to… which… which wanted to dynamically, do log sampling?
Based on how clever detection recall, though, or something like that.
**atoulme** 20:37 Omph.
So, lock sampling, there's one for deduct, and also does that, and it has some attributes about how it tags and says how many drops, how many deduct. I've also… I was wondering if there's something about the lookup processor?
Somehow it's… I'm not advocating that we do anything different here, just saying that if we start to have some sort of a sampling, the way we tag the data as it goes through the collector, if, We might want to just have a unified approach to it way down the road, not today.
**Mikołaj Świątek** 21:12 What I wanted to ask, as well, is… Can this be, scaled horizontally in some way?
Right? Because what… from what I'm reading, and I haven't paid… I've only looked at the issue right now, you have some data structure in memory that lets you do this, right? So… what happens if you want to have 5 gateway collectors that are supposed to do this? Is there some way to… sharded in a deterministic way.
**yasmine** 21:50 So, to answer your question, there's two things. First, like, the distributed state, currently, like, the state is more tracked per collector instance in memory.
So, to run it across, like, a massive fleet or, like.
like, have, many different collectors, we can use, like, the OTL gateway pattern with sticky routing, more of a shared state backend, like, RADIUS can be used in the future.
to make it, like, this reputable. But for, like, another part of this, it's also highest dropout, so, like, the tracking state is divided into 256-short architecture, allowing parallel processing, with minimal lock contention. So that's another thing.
**atoulme** 22:45 Okay.
So down the road, you would use a shared state in a Redis database, or something like that.
**yasmine** 22:51 Yeah, this can be added to the roadmap, like… again, Today, it's per, like, per collector instance, but this can be, added.
**atoulme** 23:03 It's interesting, as we're going to this type of massive ETL stuff now, it's interesting.
Okay. Yeah, any other questions, folks?
Alright, so as I said, I'm interested to… to sponsor, just because I don't know.
I'm weird. And so, I will sponsor this, I'm just gonna do this now.
I will sponsor this government?
We do have new rules around sponsoring new components to contribute, and I will admit that I haven't looked at them in the past months, so I don't remember.
I believe, besides a donation, it's great to have it already available.
What else are we missing?
Donating new components, so… I'll just post that in the chat.
**yasmine** 24:12 I will take a look at those.
**atoulme** 24:14 So, to add your components to your Pente Collector repository.
We're gonna need the GitHub handle of the sponsor, that's good. The GitHub handle the code owners. I think you said that you would be available, and you would be here for the long term to manage that component, right? You're not… you're not dropping this and going away, like, you have a lot… lots of things you want to do.
A list of other components that cover similar use cases. So, I haven't seen any, that's why I'm interested. So, if you see any, anyone here, please, comment on the issue. Some information about your component, I think you've covered that extensively, and the configuration options are well documented.
So I think we're okay.
is… anybody here reserve?
And he goes a wise.
Okay, well, in that case, you can move to open a PR to add the… just the skeleton of your component first, because that's the hardest part to drop into the repository.
And then you can add on top of it the existing code, and we will do… I'll be reviewing and helping massage that so it gets in.
**yasmine** 25:25 Okay.
Sounds good.
**atoulme** 25:28 But, alright. Thank you, Yasmin. Let's go back to Evan.
**Evan Bradley** 25:37 Yep, thank you. Okay, so… this is… okay, so I've spent, the past couple days trying to get this out. This is a revival of a… PR that I did 6-ish months ago around trying to get it so that config optional works with scalar values. I won't go into the details of Why we need to make that distinction, here, but, Pablo and Jod, you, I think you both took… a pretty good look at the last one, so I'd appreciate your review. I've got it in draft right now while I… Fix some rebase issues, just 6 months of changes, are… it's a little… little tricky to adapt to, So I'm working through that, and then I'm gonna try and get a couple follow-up PRs just to show how this is used in the Exporter Helper and in… a couple other places. I guess, just while we have the call here, are there… Any initial comments? I know, Jad, you and I talked about this a little bit on Monday. I'm not sure if you… Have thought of anything since then, or… If you're just gonna take a look at the PR.
**Jade Guiton** 26:48 Yeah, I mean, I've been taking a look, Since the beginning of the call, and… Generally, it's still my exact same thoughts as the previous PR, so, like… I still think it's not wise to… to… Have this design where we're kind of locking ourselves into I guess it's just less flexible than it… Could be mostly for the sake of potentially later adding schema capabilities.
But it is still technically enough to meet the requirements for config optional, so I will not block the PR on that, if… Yeah.
basically the same comments I made before.
**Evan Bradley** 27:36 Sure. So, for schema translation capability, I mean, you have to consider this isn't intended to replace, the existing Unmercial.
It's a… so the existing unmarshaller interface, this is a complement to that, and it's really just for these cases where you have a struct wrapping a scalar value, and you want to… kind of remove the… you don't want the struct to have a YAML representation. For these schema translation things, I think we would need an entirely different interface. If you remember, I kind of… demonstrated that with, like, a POC in the past, but I don't… I think that we can just continue to use Unmarshall for schema translations right now. And for types that are… Not… so let's say that you have… a name type, and you want to unmarshall it a specific way, you can still use the, what do you call it? There's specific… un-martialer interfaces that you can still call, and I have tests to verify that those still work.
So basically the, the call to decode.
will invoke those on the nested type, and so your… again, the only thing that the scalar on Marshaller does is just make sure that when you have a wrapper type around that scalar value, you're not required to… have a, YAML representation for that wrapper.
**Jade Guiton** 29:09 Yeah, if that's purely the only use case we want to support, then I think this is fine. It's just that even… even config optional is not like that, right? Because… Well, I guess it's probably like that at the moment, but I think the idea was that eventually we wanted to support setting to null to explicitly disable an optional.
Which right now is only barely possible if you set the underlying type to be a pointer to a scalar.
It's a little bit hacky.
And, yeah, I'm not really sure what you mean by the schema translations. I guess I haven't reread all of our discussions as thoroughly.
But, but yeah, I'll comment on the PR.
With hopefully an abridged version of my opinion, which is… you know, still not blocking, as I said, because it does meet… the PR does meet the requirements.
Okay. Because I don't want to publish an interface that people might be like.
hey, I don't… I can't do what I want to do with this.
Later, essentially.
**Evan Bradley** 30:22 Right, so the schema translation thing was just that in unMarshall, right, you're able to… you get a raw… you get raw access to the map, and you can change that before unmarshalling. And again, this is meant to be complementary to that. This really is very specifically for… I have this kind of wrapper type, it's very much like optional.
But maybe it does something slightly different. But I want to wrap a scalar value, and I want to make it so that you can essentially assign a YAML scalar value to a struct.
That's really the translation we need to do here.
And for the null case, I have actually encoded that this has the same semantics as pointers, where setting null will cause the optional to be none. And you don't have to change the generic type or anything, so an optional of int… setting that field to null means that the optional is disabled, and so you don't have to use, you don't have to use a pointer, and you don't have to use 0 to indicate that the, the integer shouldn't be set. 0 would be a valid… Value for that field.
**Jade Guiton** 31:27 Oh, okay. I… I haven't… I mean, I only took a brief look at your PR, but I thought it was decoding into a scaler With the provided type, which doesn't seem possible if the input is null .
**Evan Bradley** 31:45 So, if the input is null , I have a specific case in there. We… some… I don't remember why.
**Jade Guiton** 31:50 It's on the truck.
**Evan Bradley** 31:50 translates that into a… okay, yeah, yeah, yeah. We have a map, and if the map is nil, that's null in YAML, and then that gets just passed as nil into… on Marshall Scaler.
**Jade Guiton** 32:01 Right, because we have this additional hook that turns nils into maps or something.
Okay, yeah.
**Evan Bradley** 32:08 Yeah, that's why it took me a couple days. This is a, delicate.
Okay, anyway, I guess we can talk more on the PR, but I do think that this is… this is a good solution that the problem… for the problem that we're facing specifically. I'm not gonna pretend that it's gonna… it's gonna solve all possible use cases, but we still do have on Marshall, and that's still that, like, escape hatch, and you can do, you know, whatever the heck you want with the comp map conf.
Before, before it gets merged into your… your struct. This is specifically, again, for the case where you want to somehow map a scalar value in YAML to a… struct in Go.
**Jade Guiton** 32:51 Yeah, yeah, the problem is just that, yeah, like, unbarshall doesn't work at all if you have a scalar input.
**Evan Bradley** 32:57 Right.
**Jade Guiton** 32:58 Anyway, yeah, I'll plug on the PR, as usual.
I think you people are interested in the details of these PRs.
It sounds like.
**Evan Bradley** 33:11 Well, I mean, this is meeting's for everyone to talk, right? But, yeah, I agree, we shouldn't take up too much more time. Anyway, thank you for taking a look at that.
Dakota, you're next.
**atoulme** 33:23 But, of course, it was interesting to me.
**Jade Guiton** 33:28 That's good.
**dpaasman** 33:31 Cool.
Yeah, my topic real quick. A few weeks ago, I talked about adding a new metric to the universal component telemetry to measure the size of log bodies flowing through the pipeline, just because measuring the entire P data disrupt isn't entirely representative of the size of data.
That was scraped.
So I brought that issue up a few weeks ago. I've opened up a PR since then, implementing this. It's been open for a little bit now. Gotten some feedback so far on naming.
But otherwise, just looking for some more reviewers, and thank you, Israel. Looks like you started reviewing this during the call, so thank you for that. I'll start working through your feedback.
But yeah, otherwise, if anyone else is interested in this and interested in reviewing, I would greatly appreciate it.
And also, happy to discuss aspects of this more.
**atoulme** 34:30 Sure, can I ask you why we care about this?
**dpaasman** 34:35 Why we care about… Add in this metric.
**atoulme** 34:38 Yeah, yeah, yeah.
**dpaasman** 34:41 Yeah, yeah, so, you know, when you're scraping When you're scraping telemetry, specifically logs, we're taking that log data and kind of putting it into this P data structure, which isn't, like, a total… totally accurate, accurate one-to-one representation of the data that was originally scraped. And then we're also emitting this. We have the… we have the existing sizer metric, right, which is measuring the size of telemetry flowing through the collector.
But for the case of logs, it's measuring the entire P data struct, which is adding in timestamps, different attributes.
additional information that wasn't present on the original log data that was scraped by the receivers.
And so if you're using that metric from the standpoint of trying to understand, like, how much data is being scraped, billing and just capacity planning. That P data isn't totally accurate. If anything, it's a bit inflated from what the numbers Yeah. Likely were originally. So, that's the goal of this metric, is to solve that issue of just having something more accurate to what was originally scraped by the collector.
**atoulme** 35:57 Okay.
**Jade Guiton** 36:01 Yeah, like, if we want an accurate representation of what was created by the collector, it should be… Like, it would kind of need to be a receiver-specific metric.
Because receivers, we will… Like, scrape different formats.
Like, maybe the… looking at just the protobuf body representation is more representative of the input, but… If you have the file log receiver, and you're scraping a line of text and then parsing that.
It's still not exactly… Representative of the work that was… Thought on the input.
Yeah.
**dpaasman** 36:41 No, that… That is definitely a valid, no valid pushback on this.
I would say that… You know, it's… To me, there's kind of a balance here of… Implementing this per receiver, or… doing it more generally here. You know, obviously this is a bit faster than going through every single receiver component and defining a new, scraper metric.
Another aspect to that is there are some components, receiver components out there that have an option for, collecting raw bodies only. So, like, when it scrapes data, it doesn't process the data at all, it just puts it as is into the body of the blog.
So there are some components out there like that already, like the Windows Event Log Receiver.
Which would fit very naturally with this sort of metric, because all their data is just in the body.
**Jade Guiton** 37:46 I see.
**dpaasman** 37:48 So, yeah, there's that aspect to it as well.
**Kells Kearney** 37:54 Apologies.
The, this metric, would this potentially be used for, like, for instance, if I take a look at, like, triple and bind playing, they do use, metrics like this for ingestion purposes, and then determining, kind of like, terabytes per day metric counting.
Hmm.
Is that for this purpose as well, too? So it avoids, like, any double counting with, you know, you send… you send something to… Through a, a pipeline.
that actually goes to, like, a connector, and then, pushes that data through. It avoids, like, double-counting things as well, too, right?
**dpaasman** 38:30 Yeah, this would avoid the double counting, assuming that you're looking at the, the correct component, because this is on a per component basis, so if you're looking at it as it's coming out of the receiver, you know, that would avoid the double counting issue.
You can also use it to see, like.
how different components might be altering the size of the body. I think that's more a consequence of this PR, not necessarily a driving factor of it.
Okay.
**Andy Keller** 38:58 I can… I can add a little more perspective as well, Other telemetry types, like metrics and traces, for example, don't… don't really have the same kind of original size concept, you know, it's… a metric is… A number, so it's, like, raw size would… Be a size of the number, or size of… You know, maybe multiple data points or something, but, So it makes sense if you're… you're trying to look at throughput and usage or something like that, to be looking at OTLP, because there really isn't another thing that Really makes sense, but logs are kind of special in that they generally originate in Either, you know, text or binary form in a very measurable way that… I think it makes sense to have… Another metric that is capturing… is trying to capture that, Instead of the LTLP structure, which, logs… which, sorry, metrics and traces we use.
**atoulme** 40:08 Thanks. Right, looks like clocks continue to be special, huh?
Okay, good to know. Folks, please review help, if you have any interest in disease.
I think there's, had a light discussion about this with, Dimitri on the side recently, and he mentioned there's something about the sizer in the batch element of the exporter helper. We could also… We could have a discussion about that, because the sizer is based on that proto-marshalling of the logs, and we… maybe, for example, for our own use cases for the Splunk HEC exporter, we'd want to be sizing things according to the payload, according to HEC. So, similar to this, but different.
We will have some sort of challenge there.
So, to me, that sounds pretty relevant.
Thank you.
Anything else?
**dpaasman** 41:03 No. Thanks for the… thanks for the discussion.
**atoulme** 41:06 Awesome. Miklash.
**Mikołaj Świątek** 41:09 Right, I've taken up the mantle of trying to stabilize contact HDP.
This is more of a PSA at this point, if you have, if you, in your heart, you haven't found an issue, but in your heart lies a breaking change to the config HCP struct that you'd really like to have there, you know, please make your voice heard under there. There's also, like, one thing in there that's not done that I see Evan wants to discuss, and I can't I kind of also want to discuss it, because I'm not… Fully sure what we want to do, exactly.
Because it's, what you link there is about the, making the Keep Alive stuff optional, right?
Hold on?
**Evan Bradley** 41:59 Yes, my… my question was a little… was slightly different than that, but yes. And, I will probably be… I'm gonna do a comb through of the struct. I suspect there's probably a couple more things that we probably want to fix before we make it stable. Just a… just a heads up. I'll be doing that very, very soon here.
**Mikołaj Świątek** 42:16 just for clarity, for clarity, we can't touch the YAML struct, because it's used in stable components.
**Evan Bradley** 42:26 That's where I'm a little… conf… I just… I… I realize that we made that decision a while ago, but I'm realizing now that I'm not… I'm not clear how well we've been, sticking to that. I'll be honest, I kind of forgot about the fact that… so, the fact that the… module isn't stable, but the component is stable is, I think something I would like to codify a little bit better. I've definitely been merging, or not merging, but approving and issuing PRs with breaking changes as if there's no stable component using them.
So, I… I would have to go back and check that, but the… even if you look at, like, the OTLP components, they have a… what do you call it? Part of the component is in development for profiles.
So, how does that… I guess my question is, and what we haven't codified, is… If… so, development means you can break things.
Stable means you can't, but how do you determine… what's the interplay between those? Is profile… what does it mean for profiles to be in development if you're not able to change any of the config options? Or what does it mean for something to be stable if part of it is in development?
And I'm not clear on that, because a lot of components have different stability levels for different, what do you call it? For different, signals.
**Mikołaj Świątek** 43:57 We also talked about this with KubeCon, right? There's a difference between config stability and data format stability. Like, when I say here that profiles are… unstable, I… what I hear is that the… what is being emitted from the actual component might change format, or, like, the data might have a different shape. It also, like, means for some components that… there are some components which have, like, completely disparate They're essentially, like, two different components glued together because of, of the, subject matter, essentially, right? If you're, like.
getting… getting metrics versus getting logs from using, like, a SQL receiver is quite different, and one of the… one of those is, like, beta, and the other is, like, in development or alpha, for example. So… So I can see… I can see that point, and it kind of makes sense for signals, because signals are explicitly allowed to have different stability levels.
But… For config HCP, I… I would hesitate before breaking stuff in the supposedly stable, like, OTLP receiver.
**Evan Bradley** 45:16 So, well, that's where I'm… so the signals are declared stable for the OTLP receiver, but the OTLP receiver itself is V, you know, 0150 still.
Like, the module.
Does that make it a stable component, or… I guess I want clarification. I was under the impression it was not stable.
**Mikołaj Świątek** 45:39 I honestly am not sure, either. Is there anyone in this call? Yeah, okay, the expert, please.
**atoulme** 45:46 No, not an expert, more like an historian. The main thing is that we screwed up, we made a OTLP exporter.
and receivers… Stable by mistake.
And we should not.
And they were not ready.
And they are the only thing that are stable in… in here that would… That would somehow depend on config HTTP, so they are in contravention of all the guidelines… the guidelines we have set afterwards, which were that you cannot mark something stable if it has unstable dependencies.
And so now I'll be paying for this. So, I think we need to move configHTP stable ASAP. It's been waiting for too long. There's a ton of PRs in the OpenT collector repository related to some Minute changes to configure HTTP that are worth reviewing. Unfortunately, I think you're not going to have a very good time. I already found two without trying.
**Mikołaj Świątek** 46:46 I review… I did review them, but I did review them with an eye for, does this require breaking changes in the API? And as far as I can tell, none of them do. Some of them are a little bit complex, like Josh McDonald has some complex ideas, but those also don't require breaking changes, so we're at least good with that.
**atoulme** 47:09 Alright, then, in that case, I would say that… I'm very impatient about all of this. I would say we should move it to stable and be done, and start to move on to .X, and… Be good about it.
**Mikołaj Świątek** 47:22 I personally agree. Unfortunately, Pablo left, and he disagreed last time. He thinks this Keep Alive stuff should actually be done. I think the Keep Alive stuff is okay. I personally am perfectly fine keeping it the way it is right now, which is, like, basically one-to-one with what the standard library wants.
Like, the attributes are basically identical.
But we can move that to… that discussion can also, like, move to an issue. I also don't want to eat all of the time. But here, like, the issue here is the right place, and it is actually going on in the issue right now, so you can make your voices heard in there.
**atoulme** 47:59 I will go and do that. Thank you, Miklash. Do you want to take the next item, please?
**Mikołaj Świątek** 48:04 Yeah, yeah, yeah. The next one is, it's like a… Again, I'm informing. I wanna… for those of us who hate Windows, you can avert your eyes, but there's a thing in Windows called a named pipe.
And it's not exactly similar… not exact… not… not… it's not exactly a Unix domain socket, but it's close enough that you can kind of pretend it's a Unix domain socket.
And I'm adding that as a transport to ConfigNet for those of us who have to run the collector on Windows and also can't guarantee that it's a new enough version of Windows to act… to have actual, Unix domain sockets available. Anyone's interested, want to see, want to review, there's a pull request in there that is, like, very uninteresting.
There you go.
**atoulme** 48:56 Thank you.
**Mikołaj Świątek** 48:56 Yeah, Tiffany?
**Tiffany Hrabusa** 48:59 Hello!
I'm here just to give a quick update on the collector docs refactoring.
We did not make a lot of progress, in the early part of the year.
Mostly down to my availability, but things are starting to pick up now.
This is just my regular flea, that if there is a section of the docs that you are especially interested in, or have worked on, or have had trouble with customers because it's not complete, now would be a good time to speak up. I've linked to what the plan… our ambitious plan was last year for Phase 2 and the current open issues.
We will be adding more PRs soon. Thank you to Jad for consistently reviewing these PRs. If anyone else would like to jump in, the, collector approvers are always tagged on those PRs, so feel free. Thank you.
**atoulme** 50:09 Okay, any questions for Tiffany?
Awesome. Alright, Miklas, you're back.
**Mikołaj Świątek** 50:20 Yeah, it's me again.
Again, PSA, the partial config reload RFC is progressing. There's some activity. We are converging on something that I think might be merged soon, so again, if you're putting off looking at it, if you have an interest, or if you're deeply offended by the thing we are doing in there, you know.
Reminder.
That might, might soon go in, in, in some form, so make your voice heard.
If you have opinions about what's in there. That's it. Thanks.
**atoulme** 51:01 So, is this really just waiting on spellcheck, or what?
**Mikołaj Świątek** 51:05 It has actually a fair amount of feedback to it right now, but the feedback that exists there is mostly kind of… Addressing corners.
Like, I think the broad idea of it and the reasoning for it is… Cool.
Right, no.
**atoulme** 51:24 Okay, understood. So… do we want… I'm wondering if it's thoughtful to continue to have more discussion on that PR, or do you want to get it merged ASAP to move to a bit more of a discussion about how to go about it?
**Mikołaj Świątek** 51:39 No, it doesn't have to be merged right now. I'd rather have more… I'd rather it be more airtight than rush. The implementation is, in some respects, simpler than agreeing, like, that yes, this is actually what we want to do, and we want to do it for these reasons.
The implementation is, despite those POC PRs being pretty big, a lot of them are just tests.
**atoulme** 52:06 Dude.
Yeah, it looks like the PSCPR is really big, because it just has…
**Mikołaj Świątek** 52:14 It also has… that one also has everything. There's also another one which only has the first phase of the change, and that one's, like, 600 lines of actual code doing something, so it's not that bad.
**atoulme** 52:32 Alright.
Any… Anything else on that?
Cool. Anything else you folks would like to discuss?
Chat's clear, everything's clear. Alright. Thanks, everybody. Have a great day, good night. Take care.
**Evan Bradley** 52:52 Bye everyone.
**Andy Keller** 52:53 See ya.
