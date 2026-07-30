SIG: Collector SIG
Date: 2025-11-26
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Pablo Baeyens 00:02:03 Hey.
João Duarte 00:02:06 I'm a home.
Evan Bradley 00:02:09 Hi, everybody.
Pablo Baeyens 00:04:15 Could we get started?
Evan Bradley 00:04:20 Let's do it.
Pablo Baeyens 00:04:23 Yay, so I… We talked about this a couple of weeks ago, I put, First time slot of 15 minutes to, go through the… issues related to the Phase 1 of stability, for components. So, as a reminder.
This is the list of… components that we are focusing on, and, well, Bradon created a board, I've… Tweak the statuses so that… the… Are a bit more granular, but otherwise… Yeah, it's Braden's work, thank you.
And… Man, let me… share my… green… Just this first time.
Can you see my screen?
Jade Guiton 00:05:30 Yes.
Pablo Baeyens 00:05:31 Okay, cool.
So… This is the board, and I could… Discussion needed as one of the… statuses, then if there's been discussion, or no discussion is needed, it's workable.
Then, in progress… Once it is ready for review, there's waiting for reviews, and then done.
So… I tried to put a few of this in discussion native based on what the issues look like, but Workable is what used to be to-do, so there may be some… That are currently marked as workable, that are… Actually, under discussion, or discussion needed.
And then another thing I'll mention, I put this… label meta-issue for things that, children, so that we could look at Actual things that need to be worked on, and not just, like, meta issues that track marking the Prometheus receiver, stable, or stuff like that.
Fairly OddParents (ca-wat-brt3) 00:06:51 So… Is there a blocked state?
Pablo Baeyens 00:06:54 There is no block state, but I cannot, Actually, let's… let's do it right now, but… Yeah.
Fairly OddParents (ca-wat-brt3) 00:07:03 There's a couple of those host metrics ones that are blocked. I can… I can mark them appropriately.
Pablo Baeyens 00:07:09 Okay, so let me… make this… Red, I guess.
Okay, there's also the blocked functionality on GitHub, but I don't know how to… Show it here.
But you can… so let me… Let's say… This one… There's another issue on semantic conventions.
the… Shoot… Block it, so let's say, there's… Good blockade.
You can do… on relationships marked as BlockFi.
you select the repository… I don't know what level of permissions you need for this, I assume three editors can do it.
And you can mark it. Let's see if the… Show something. Oh, okay, so you can…
Fairly OddParents (ca-wat-brt3) 00:08:30 Oh, interesting.
Pablo Baeyens 00:08:32 You can see the… Little… Forbidden icon here, and .
Fairly OddParents (ca-wat-brt3) 00:08:38 Okay.
Pablo Baeyens 00:08:39 And we… Okay, yeah, so you can… filter by blocked? It's just a different thing from status.
So maybe we can just use that.
Fairly OddParents (ca-wat-brt3) 00:08:51 Yeah, sure, that's fine. I didn't realize it worked like that.
That'll be fine.
Pablo Baeyens 00:09:01 And I don't know what to use exactly this time for. One of the things I wanted to discuss was, having people that flesh out the required issues for each component, I guess we can, talk about that in the 5 minutes that remain, so there's… Two remaining that don't have, people. One of them is the Kubernetes attributes processor.
And the other one is the resource detection processor.
You don't need to be, code owner for this, necessarily. It's more like a product management thing, so… I don't know, if… it's going to be easier if you're a creator because of the permissions and such, but, if you want to volunteer, I guess you can… Sorry, not here. You can comment on the… Individual issues listed here.
Christos Markou 00:10:06 I can do the, cage attributes one.
Pablo Baeyens 00:10:11 Okay.
I think that's you, Christos?
Christos Markou 00:10:18 Yeah, right.
Pablo Baeyens 00:10:20 Sorry, I cannot see a figure because of the voice, but I cannot see who's speaking.
I could volunteer for the research detection processor.
To be honest.
Yeah, I guess… The people that have volunteered could… if you can look at the… Ones that are in workable states, that are for your component, Check that the status is okay, that would be… Helpful.
on… Yeah, I don't know, if there's a specific issue, or… PR that you want a review for, or something related to these components and their stability, I guess.
We still have 5 minutes.
If not, we can… Keep it shorter today.
Christos Markou 00:11:18 I have a question, are, should we, have a look and check How is the staffing of those components?
And I don't know what actions we could take, but for example, I know that the issues detection processor is not, like, there is no super active development happening, over the past months, and probably the… only David Ashpole is active right now. The other main… the other co-donor, has not been active recently.
Pablo Baeyens 00:11:55 So you mean, with stuffing, you mean the code owners?
Christos Markou 00:11:59 Yeah, and if we should somehow, like.
advertise this, or just mark the components with a seeking for code owners, more code owners, label, or, the thing that we add in the README, for example.
Pablo Baeyens 00:12:13 Right. Okay.
Fairly OddParents (ca-wat-brt3) 00:12:18 I believe the file log receiver also only has one code owner right now.
Andre is the only code owner.
Pablo Baeyens 00:12:42 Okay, I think the other ones should be fine. So the host metrics receiver has Dimitri and Braden.
Prometheus Receiver has… Four people, including David on Arthur.
Kubernetes Attributes has 4 people… On filter and transform processor health.
4 people each.
I can volunteer to open a PR… Find the… seeking good owners label… And if anybody on the call is interested in becoming a co-owner for… any of the components on Phase 1, but especially the ones Crystal and I just mentioned, Feel free to… To reach out, autoCollector Dev, for example.
Is there anything else we should do for… Trying to find code owners for these components?
I guess we can start with that.
Okay, any other… topics about… stability.
Alright, then I'll keep talking about a different topic.
So let me share my screen again… So, we discussed this… in past weeks, I filed a PR, to… change the requirements to contribute new components, and there's a few threads that are open and I wanted to discuss here. So, first… Eyes.
GitHub allows… I have moved things from the contributing .md to a new separate doc for new components.
And, before we go into the comments, the changes are… it's now recommended that you would host your component outside of collector contrib.
And this basically has some instructions, maybe I can switch to D.
Preview.
Yeah, so these are some instructions on how to do that.
Then, there's a change on the sponsor wording saying that ideally it would be from a different company.
And if the sponsor and the component… the person proposing the component are from the same company.
You should have approval from other approvers and maintainers?
And then… There's a clarification here that… If an in-development component does not make progress towards all fault stability, it may be considered unmaintained and be removed.
So, now, in terms of the things… that I wanted to discuss… there's this thread that Andrew opened.
And Christos also had some comments about it.
So… We could just… Outright require that the sponsor is from a different company than the, person proposing the component.
So… what Andrew proposes is you need three co-owners, one of them is an approver maintainer.
And, you need an approver maintainer to sponsor that component.
And, andrew's idea is that, the sponsor Does not, Has no further role other than approving the proposal.
And maybe, Christos, if you want to summarize your points here?
Christos Markou 00:17:30 Yeah, I would… I mean, I see the point of having the sponsor just to, like, give the green light, but I think I'm not sure how meaningful that would be. It's not really a sponsor. It's not really a sponsorship. So, I would, like, suggest Maybe we can discuss it.
I would suggest that the sponsor should continue, like, reviewing the initial implementation.
And after the initial implementation is done, of course, the sponsor can… is not required to become a co-owner or whatever. And the reason for this is that, otherwise it can be… super easy for, like, approvers to just say, I sponsor this, without an actual cost for them, or whatever. So, the point is that if I'm willing to sponsor something.
I should be able to spend some time on it, which means that I find this interesting. I'm not just sponsoring it because I just want to sponsor it, or whatever. So that's, that's my, suggestion there, if that makes sense.
Fairly OddParents (ca-wat-brt3) 00:18:40 Yeah, I'm kind of in agreement there, because the… The idea that the sponsor Doesn't need to… like.
be… I mean, like, the definition of the word sponsor no longer applies to that, I think.
like, the sponsor isn't sponsoring anything, because sponsor means you're providing some kind of effort, or some sort of return on… on including the component. So this feels like it actually is against the goal of this PR, where the goal of this PR is to raise the bar for how a component gets in to contribib.
that change to what a sponsor means sort of actually lowers the bar back down again. Like, someone who's saying sponsor doesn't actually need to do anything.
Amanda Murphy 00:19:28 Have there been issues with the bar being too low?
Fairly OddParents (ca-wat-brt3) 00:19:33 For most of the lifetime of this repo, yeah.
Amanda Murphy 00:19:39 Is it that people aren't maintaining their components?
Fairly OddParents (ca-wat-brt3) 00:19:47 Yes?
Pablo Baeyens 00:19:47 Yeah.
Fairly OddParents (ca-wat-brt3) 00:19:48 And there's a lot to that.
Pablo Baeyens 00:19:52 It's also the added… Cost for existing approvers and maintainers on, Sponsoring these components, or, like, mentoring these new people, with the component?
I, I think you… points are reasonable, Christos. I guess if we were to do the change that Andrew is proposing, we should have a way to… measure code owner involvement more thoroughly, which is something that, well, we've already discussed several times, and will do eventually, but… Yeah, maybe… Maybe right now, it's not the…
Christos Markou 00:20:42 Yeah, just to be clear, I agree with the suggestion of Andrew. I would just extend it with the additional requirement that the sponsor should, like, keep an eye on, review the initial implementation, without requiring them to become co-donors eventually.
So, maybe the… in my comment, I left my suggestion there.
Right. Maybe the wording is not really accurate, but yeah, we can discuss on this.
Pablo Baeyens 00:21:13 Okay, so I'll… make a comment here about what we discussed today, and wait for Andrew to reply, and we can move forward here.
And then the other thing that I want to discuss is this comment by Christus.
So right now, I changed things to recommend posting outside of the repository. I did that because I was not sure that there was consensus for just outright requiring that you first host it outside, and then you… You donated… I would be fine with being more aggressive here, but I wanted to hear if other people are… Okay with that more aggressive change.
Fairly OddParents (ca-wat-brt3) 00:22:07 I'm in favor of it.
Evan Bradley 00:22:12 I would be in favor of it, too. I guess, I think it would be better motivated… do we know how many, like, new components have been added in the past 6 months, for example?
Like, I would be in favor of it if we feel like we've hit capacity in terms of… being able to sponsor new components, but if people still feel like they have capacity, then I don't think we maybe need to be quite as stringent.
Fairly OddParents (ca-wat-brt3) 00:22:39 Well, I think even before the capacity limit is hit, it's… like, having sponsored components before, there's a lot of work into the initial, like, skeleton, and, like, just getting a valid component together that would be… done… Separately. In a donation scenario. Like, you wouldn't have to go through this sort of… initial setup of, like, this is how you put together the component, this is, like, like, this XYZ thing isn't working right, you know, like, it would save a lot of work if that was all there and proven and built in a collector and worked first.
Evan Bradley 00:23:21 That's definitely fair.
I mean, I feel like we get around that just a little bit by requiring, People who propose new components to implement them, like, incrementally.
I… well, so even if there is a lot of work involved, since sponsorship is purely voluntary, I guess that's where I'm… I'm saying if we… If we feel like we're at, you know, 70% of capacity, and we think we can get to… You know, whatever level we're comfortable with for accepting these components.
Pablo Baeyens 00:23:58 I think it's not only a question of capacity, it's also… The reason I filed this is more… we have a roadmap of things that we want to do for stability. I want to free up time from, approvers and maintainers and the community in general to… to work on that roadmap, and I feel like… If we get people to work on their own on the component, and then donate it, we still can add new components, it's just… it's more clear that the work is on the person proposing the component, Rather than on the maintainers and approvers that are more focused on On this roadmap.
Evan Bradley 00:24:45 Right, no, I think that's definitely, I think that's… Fair. I guess what I'm trying to say is if, you know, there are… you know, if there's anybody on the… that is a maintainer or an approver, and that's kind of their… their focus is more of, like, a, you know, community-oriented, like, I'd like to get new components into Contrib, you know, I wouldn't want to hold them to… you know, we need you to work on, like, stability efforts instead, that's all.
In general, though, I think people are more than willing to. I've seen numerous instances where if… Somebody puts out a new component proposal, and it's taking a while, they will have it already out in a repo, and… you know, like, proved out and all that, so I think that, This isn't an unreasonable ask.
Pablo Baeyens 00:25:44 So, I think I'm going to change it to be… to have a more forceful, language, just share it widely within approvals and maintainers, and if There's somebody that is more, yeah.
component-focused, to say it in some way, and disagrees with that, they can… Complain on this VR.
Evan Bradley 00:26:09 That sounds good to me.
Pablo Baeyens 00:26:14 Alright, so… I think that's it for me, so then… Jobeless.
Your turn.
Douglas Camata 00:26:24 Yup, so I… let me share… I'll share my screen a little bit.
Oh my god, what a mess Zoom made. So I just have a few quick things to talk about. I see many people have other important things that are worth longer discussions, but please listen to me.
So, I have a few issues that I'm looking for, opinions of others. One is on the OPAMP extension.
Basically, I would like to somehow make the agents report to my backend, the raw configuration.
that they are, using. Basically, we already got the effective config, right, but that includes defaults that are injected by the collector at runtime, so a bunch of configuration that is not part of the files that users might be writing, and I'm interested in doing some cool things that would mean I need to throw away all those defaults to get Exactly to the configuration that, that users wrote.
in their files, so I have this proposal there. I already got some nice comments from Tyler, but if anybody else wants to chime in, especially when it comes to implementation ideas, because it seems to be a bit of Tyler's concern.
Please, please do so, during the issue, or we can have a thread in Slack, it's also fine for me.
Another one that I have is, more on the… it's on the supervisor. I… I would like to be able to have A kind of fallback configuration, only in case I cannot talk to the OPMP backend, so… Again, I got already some comments from Tyler here.
That, was… To use configuration files?
In the supervisor, but that… That ends up later merged with remote configuration, and I want something… exactly… That is exactly the opposite of this. I want something that will be thrown away as soon as I, can reach the OPAMP backend and potentially receive some remote configuration from there.
So again, please feel free to leave a comment in the issue, or we can talk in Slack.
And last but not least, I just have this small PR… to add a few extensions, a few common small extensions to the BPF distro. If anyone could have a look, that's highly appreciated.
And… that's it.
So, thank you, and I think we can move to Evan.
Evan Bradley 00:29:40 Alright, thank you.
So, this issue was opened up after, somebody internally was doing some stress testing on the collector for a customer setup, and kind of found that we basically have, like, a very, slow memory leak in the cumulative delta processor.
So right now, the processor, you know, as, data points are flowing through the collector, will hold onto the previous data point's value to, perform the delta conversion.
The thing is, if you're… let's say you're monitoring, like, you know, Kubernetes stats or something, and you have pods that are changing IDs a lot, you have new, you're gonna be getting new… metric streams, and as a result, the cumulative delta processor is eventually going to be holding mostly, inactive metric streams. And so, as a product of that, the memory will just, it has unbounded growth.
So, what we're proposing here is to set a 25-hour limit on… Metric point validity, and then after, you know, if a metric point hasn't been seen for that 25 hours, it's considered stale, and it's, essentially, like, garbage collected.
The goal here is that, it's a fairly, we think, conservative, default value.
Since I know that the initial proposal here from Andres is 5 minutes, but we were gonna go for 25 hours, I'm just looking at that now.
The goal here is that, let's say you're… you have some metric that is enabled, or is, it's emitted, once per day. This gives, like, an hour buffer, just in case, you know, something's late or something. But outside of that.
You know, if… The user understands how often their metrics are coming in, you can set that to be more aggressive.
The reason I'm bringing this up is I just wanted to, before pushing on this a little harder, just make sure that there weren't any… Dissenting opinions, or things that we missed, or anything like that.
Pablo Baeyens 00:31:55 So, we have… functionality equivalent to the community to Delta processor on the data exporter?
Because when we wrote that, the cumulative delta processor didn't exist.
And the default, there is, if I recall correctly, 1 hour.
And I don't think we've heard from anybody complaining about that. Like, people are… if they have this kind of edge use case where they… they send a metric very infrequently, they are able to figure it out and change the parameters.
so, just as a data point of… What do we do?
Evan Bradley 00:32:36 That's actually really helpful, because we weren't able to really come or find anybody that had, you know, used this setting in one way or another and needed to set a value. I don't know that we have strong opinions about 25 hours versus 1 hour. The only reason I would go for 25 hours is maybe if we're looking for a broader range of users, but… I mean, I would be pretty much fine with 1 hour or two, if you're saying that you get… you don't get any concerns, and you have, you know, X number of users using it.
Jade Guiton 00:33:12 I think the defaults, yeah, should kind of have a… I guess, a compromise between Performance, and how many users it… it, enables, I guess?
And I guess the question is, how often do we see these one point every 24-hour use cases?
I believe, I'm wondering, like, My understanding of how the SDKs work is that Even if there is no event, it will still emit the cumulative metric every… Every export cycle.
So, wouldn't that refresh the… the TTL… Anyway, or are there, like, receivers that we expect Emit cumulative metrics, but extremely rarely.
Evan Bradley 00:34:03 I guess it'd be mesios.
Actually, I don't… I don't know, Braden, do you know off the top of your head?
Fairly OddParents (ca-wat-brt3) 00:34:12 So, the question is, do we know of any receiver that might produce a cumulative metric at a… Like, it's such a long time frame.
Jade Guiton 00:34:22 Yeah, because my understanding is that for hotel SDKs, that shouldn't happen.
Fairly OddParents (ca-wat-brt3) 00:34:29 Right. Yeah, for Prometheus specifically, probably not, unless they have a scrape interval that is that long.
Jade Guiton 00:34:38 Right.
Fairly OddParents (ca-wat-brt3) 00:34:39 And I think, actually, they handle this. We've had to handle this for… related to start times more than cumulative delta conversion, but it's the same concept where we have to maintain a table of all, like, time series identities that we've come across and what the start time is. And the way Prometheus handles that, and that we've handled that in some of our processors is with a, like, a garbage collection interval that is automatic.
Based on the scraping interval.
Hmm.
And so, if, if we haven't seen a particular time series identity in, like, scrape interval plus a minute, or plus 10 seconds or something, then it'll get cleaned out of the cache, and I think that… I don't know if we… we probably don't have that same luxury in cumulative to delta to say dynamically based on something, but there is precedent for this sort of, like, having a default garbage collection.
Which is essentially what this is.
Jade Guiton 00:35:37 So, okay, so for OTLP, you wouldn't expect points that rarely unless someone says the export interval to 24 hours, but and for Prometheus, same thing, but for the scraping interval.
So, yeah, I guess… It's not about how often the event occurs, but… Whether there is a weird receiver, or an extremely niche configuration for OTLP or Prometheus.
that would… Amid these points this rarely.
And… So, yeah, the other side of the compromise is that If, you know, you get more metric series over those 24 hours, they're gonna accumulate in memory, even… even if they're only seen very briefly.
So, yeah, I don't have… data.
To support the idea that, it should be shorter, but yeah.
the… my thought is that it may not be just for rare events, but it would have to be, like, a very particular configuration, or a receiver, I guess.
Evan Bradley 00:36:54 That would be my expectation as well. And also the… I guess the inverse of that, which, I guess would suggest a longer… or a longer interval would be okay, is that I don't know, or I have not seen any, issues open on the cumulative delta processor saying that users are running out of memory because their long-lived collector has seen too many metric streams.
As of right now…
Fairly OddParents (ca-wat-brt3) 00:37:16 from ECS receiver, and the problem was cumulative to delta.
Evan Bradley 00:37:22 It wasn't an issue open on cumulative to Delta, but, like, the problem… that was the problem, and it was just, like, they were using the Prometheus receiver, and they're seeing a memory leak, or whatever. Like, we've seen that before.
Got it, okay, that's good to know.
I guess I looked for the wrong label.
Fairly OddParents (ca-wat-brt3) 00:37:41 I can send you the specific issue that I have in mind where I first discovered this was a thing that can happen.
Evan Bradley 00:37:46 If you could link to it in this issue, I think it would be great just to justify this change.
Fairly OddParents (ca-wat-brt3) 00:37:51 Yes.
Evan Bradley 00:37:52 If we have seen that, that would also make me lean toward, closer to 1 hour.
Fairly OddParents (ca-wat-brt3) 00:37:59 Yeah, I'm kind of in favor of one hour, because I think we're more likely to get, oh no, the collector's memory leaking issues, than, why did my cumulative metric disappear.
Evan Bradley 00:38:11 Right, for my metric that's only collected once per day, right?
Fairly OddParents (ca-wat-brt3) 00:38:13 Goodbye.
Evan Bradley 00:38:15 Josh, I see you have your hand up.
Joshua MacDonald 00:38:17 Yeah, I agree. This is almost certainly about processes that die and are just leaving memory alive in the collector. It's not a question of how often these things are reporting, it's a question of how rarely you scrape from the outside world. Like, if you're scraping, like Prometheus would, every 24 hours, well, then you really do need to remember those cubitives for 24 hours. But if you're… if you're scraping every hour, then, you know, this'll work fine. And nobody… and I don't… I'm not very familiar with users doing such a long interval anyway. So, like.
Fairly OddParents (ca-wat-brt3) 00:38:49 Probably not with me.
Joshua MacDonald 00:38:49 The risk is that you lose measurements, but there's nothing really wrong with saving that memory. It's actually a practical thing to do.
Evan Bradley 00:38:57 Okay, also a good data point.
Okay, it sounds like there's broad, agreement that we should have this, and that an hour is a good default, so I will, I'll let Andre know and keep pushing on this. Thank you for the discussion and insights, everybody.
Shh… Sean, you're next.
Shaun Remekie 00:39:28 Hey guys, thanks for having me.
Cool, so I'm interested in, well, looking for sponsorship for a new component. Also, forgive me if I sound a bit out of it, I'm, like, running, like, a 38-degree fever right now, so I might hallucinate a bit.
So I'm looking at, Acquiring sponsorship for a new component, and I'm just gonna share my screen here.
And so this component is the, AWS ECS AttributesD processor.
So this is a processor that is actually already written. It's been… it was built by, CoreLogix, and it's a processor that we've been using internally for our ECS, workflows.
For about 3 years now.
So what it does is… It allows the collector to run as a daemon set, and associate ECS attributes based on the ECS Stats API.
With, telemetry data.
Now, presently, there's no existing way to do this inside the current, Country Bomb release.
We're unable to associate, metadata if you're running as a daemon set. You have to run as a sidecar in order to associate that metadata.
So this was created in sort of direct consumer request that, you know, we have something that does this, and so we created it.
How it works, effectively, is that it… Sorry. Yeah, how it works effectively is that it uses the Docker API to fetch all the… all the running, ECS stat endpoints. So these are allocated whenever you create a container inside ECS, and they're sort of dynamically allocated as well, so there's no way to infer them. You kind of have to fetch them once they exist.
So the processor will call the Docker API, effectively, and retrieve all the metadata endpoints, and then it will scrape those metadata endpoints, and create a cache of, metadata that's associated with each container.
Then it will use the container ID, which is, Which will be provided, you know, by the user.
In the, in the telemetry data.
To associate that, that metadata with the relevant container.
And you can see that workflow there.
is effectively as calling the Docker API, and then calling the ECS Metadata API, and then associating, telemetry data and, AECS attributes.
So currently, this supports metrics, logs, and traces.
It's been tested intensely with logs, because it was created specifically, 4 logs to start with, but we recently added, Metric and trace support, as well as profiles.
And just a brief look at the config there, like I said before, the main mechanism for associating telemetry data with the ECS attributes is the container ID, and so in the configuration for this processor, there is a mechanism to specify where to look for the container ID, in effectively telling it what resource attribute to check for the container ID.
And that is, like, the main element of configuration. The other bit is… effectively telling it what ECS attributes you want to, Associates, and you can do this using, regular expressions.
The list of attributes that are supported are also found here in the, in the, in the issue.
As well as, the code owners and so on.
Like I said, this has been, running with several of our clients for about 3 years, so it has been rigorously tested, and so we are interested in moving away from having to build our own distribution just to support, an ECS integration, and so that's one of the main reasons for us to, try and get this thing, Added to, the main distribution.
Any questions, guys?
Dmitrii Anoshin 00:43:46 As far as I understood, this is similar to Cumulated Satribe's processor that we currently have, right?
Shaun Remekie 00:43:53 Yes and no. So the Kubernetes attributes process, yes, it is able to associate metadata based on the context provided through OTLP.
Whereas that is not currently possible with ECS.
So there's a… while it has the same function, the mechanism for associating the metadata is distinctly different.
Dmitrii Anoshin 00:44:26 So it only works on the daemon set, or, like, on the local, Only enriches the data for the… local telemetry, right? Is that what you're saying?
Shaun Remekie 00:44:38 Yes, effectively, it, it's specifically built for a daemon set, running as, the collector as a daemon set. Okay.
Dmitrii Anoshin 00:44:47 Sorry, we have the result detection process, which kind of… also provide these similar capabilities, but I guess it's also a bit different, right?
Shaun Remekie 00:44:57 Yeah, so resource detection doesn't work in this… so if you imagine for a sec, you're collecting logs on ECS via, a daemon set, a collector running as a daemon set. You've pointed the collector to the log, path where Docker stores its logs.
You're collecting logs, and now you're trying to figure out where those logs came from.
within the OpenTelemetry collector.
The only mechanism to tell the collector where those logs came from is the actual log path that it took. Sorry, the log path that it took the logs from, but… without this… without this particular, processor, there's no way for the collector to use that log path to associate telemetry data. The resource detection, Processor isn't able to do it.
So there's a lack of… a distinct lack of, a mechanism to associate the metadata. This is just a known issue in ECS in general.
So the approach that is recommended by AWS is to use a sidecar, which… when, you know, speaking to our clients, they would prefer to be… to have this done as a daemon set, but AWS themselves has not really offered a solution.
Christos Markou 00:46:18 Could that… I see that it connects to the Docker API, so to me, it looks Docker-specific. Could that be a generic Docker Attributes Processor, similar to what the Kubernetes Attributes Processor is. So, the configuration would be that here is the Docker API endpoint, and the processor can fetch metadata from this, store them, cast them, and then does the… do the enrichment.
accordingly. Would that work? Or it should be AWS-specific for any reasons?
Shaun Remekie 00:46:57 So yeah, that's a good question. I think when we built it, it was… we built it specific to, to ECS.
In this context, because there are… there's a distinct number of attributes that are associated with ECS.
And there are distinct attributes that are associated with, With the Docker API specifically.
For our purposes, we needed the ECS attributes, and the only way to get to them was via the Docker API and, sort of fetching the… the ECS metadata endpoint.
from the Docker API, and then calling that.
It is… yes, it is entirely possible to build something that just calls the Docker API, but it wouldn't really solve the ECS problem.
Christos Markou 00:47:43 Okay, yeah, I see.
Fairly OddParents (ca-wat-brt3) 00:47:46 I think maybe I just misunderstood something earlier where you said that the resource detection processor doesn't work, and the reason was that the resource detection processor can't get, like, a log file path or something? Can you repeat that?
Shaun Remekie 00:48:03 Oh, so I was saying that it… there's no mechanism for it to associate metadata.
In ECS, there's no mechanism for it to associate the method. Alright, let me see if I can articulate this a bit better.
With the resource detection, I believe it functions in the same sort of vein as, like, the… the sidecar approach. Effectively, you deploy it inside a… Deployed inside a sidecar, it runs, it detects resource attributes.
Now, if you're… if you're scraping logs from the… or, sorry, collecting logs from, a daemon set approach.
Resource detection will… Only be able to get the… Metadata of the running collector.
So it only knows… it only sees the collector, it's not able to see all the other containers running on the instance, and as such, even though it's collecting logs from everything on the instance, it will never be able to associate the metadata With the, with the log data itself, because all it's seeing is its own metadata.
That's if it's running as a daemon sense. If you run it inside a sidecar.
That works fine, but it's kind of not… we're trying to avoid that.
Fairly OddParents (ca-wat-brt3) 00:49:28 And why does… Your own processor versus this being a resource detector change that?
Shaun Remekie 00:49:37 So, sorry, why does the… why does this…
Fairly OddParents (ca-wat-brt3) 00:49:40 Like, you stayed What I'm trying to get at is, like, this is its own processor for the purpose of, like, because, like, it can't do something that the resource detection processor can't do, versus this just being another entry in resource detector.
Shaun Remekie 00:50:02 Yeah, I don't have an answer to that, to be honest.
It's looking at the resource detector. At the time, it was… The decision was taken to build it out as its own processor.
I'm not sure what it would take, effectively, to build out or adjust the resource, the resource detection processor to function in the way that we need it to.
Or if that would be… something that would be conducive to, you know, the OpenTelemetry community in general, if that would be allowed.
And so I think some of those things were taken into consideration, and we just went, let's just build a processor.
DA Dmitrii Anoshin 00:50:39 I think, the problem… like, the conceptual difference here is that when we, take, the sort of detection processor, we say that like, everything… all the data is local. Like, all the data that's coming through the resource detection processor, we enrich it with local entities. For example, it's coming through collector running as a Kubernetes node, we enrich it with an entity called Kubernetes Node, or Kubernetes, like, for example, AWS Cloud VM, if it runs to Cloud VM.
Here, it's a bit different, I guess. We are… Working on the… entities, we are enriching entities that are coming from the outside, so they are not local. Like, for example, container.
Shaun Remekie 00:51:25 We want to enrich…
DA Dmitrii Anoshin 00:51:27 Metadata for the specific container.
but it's different metadata for each telemetry coming from different containers, right? So in that sense, it's closer to commercialized attributes receiver, running as a daemon set, it's just different enrichment model. It doesn't support the context as a source, as association source, like client context, essentially, client IP address. It just uses different, different, like, Docker API and those things, like, different association approach. Is that correct understanding?
Shaun Remekie 00:52:07 Yeah, that's exactly right. It serves, like, like you said, it serves the same exact purpose as the, as the Kubernetes attributes processor. Just the mechanism for associating metadata is different, and it's a lot more strict. There's not a lot of options in ECS for associating metadata.
So, so that's why.
DA Dmitrii Anoshin 00:52:30 Okay, I guess that's… makes sense to make it, like, a separate, processor, it will be similar processor… similar to Kubernetes Attributes Processor, it just will be, like, EKS, I guess, attributes processor.
AKS, ECS. AWS is yes. Why? There is a D at the end, I'm curious.
Shaun Remekie 00:52:51 Oh, I just, just, just as where Damon said.
But I'm not, I'm not married to the name. We can always change it.
Jade Guiton 00:53:00 Is the main… the main difference from the Kubernetes attributes for SSR? Is the main difference the way… that the container ID is obtained, or is it mostly just that it's using the ECS API versus the Kubernetes API?
Shaun Remekie 00:53:15 So yeah, you could say it's using the… it's because it's using the, the ECS, stats APIs, or sorry, metadata APIs.
And on its own, and this is one of the major limitations, on its own, it's not really able to, identify the container ID. Like, the container ID has to be specified, as a part of the configuration. It's like… basically telling it where to look for that container ID, whereas with the… Kubernetes, attributes processor, it's sort of automatic. You have a lot more options for detecting it automatically.
And again, these are just limitations within ECS, so we've done some research into trying to figure out how we could, gain more context from ECS, but it's literally just not there.
Jade Guiton 00:54:04 So how? It sounds… it sounds like the association rules in the KH attribute processor are basically a superset of what this processor offers, and the major difference that would warrant making it a different processor It's just the data source is completely different, essentially.
Okay.
DA Dmitrii Anoshin 00:54:23 how… so the user would have to manually specify the association for the container ID, like, and how… how do you typically do it? Like, how do you set container ID?
Shaun Remekie 00:54:34 Okay, so… Sorry. So, one of the… like I said, initially, when we created this, this was just created for the logs workflow. We wanted to be able to collect logs, as Damon said. And so, this example here.
shows how we would do that. So we just use the file log receiver, we read the log file. Now, in… in the Docker container log file path.
It normally has the container ID. Yeah. And so then, as a part of the attributes processor configuration, we just say, hey, look for the container ID in the log file path. And there's provisions actually built into it, that if you give it a log file path, it will just extract the container ID.
DA Dmitrii Anoshin 00:55:10 Sorry, and that's pretty much the same approach that we do for Kubernetes Attributes Proster for the, for the logs.
Shaun Remekie 00:55:18 Oh, okay. So, take it from the path.
DA Dmitrii Anoshin 00:55:20 It's the same. So, I'm curious about other signals. Sorry, we have too many… Too… not much time, but…
Shaun Remekie 00:55:27 Okay, okay.
DA Dmitrii Anoshin 00:55:27 We'll take it offline. But anyway, I think it's good. I'm, like, I'm supportive, I just don't have enough capacity to sponsor it officially. If anyone else has it, that would be great. If not, maybe we'll figure something out, but I, in general, it seems… Pretty reasonable to add this kind of cluster, from my perspective.
Shaun Remekie 00:55:46 Okay, thank you.
Amanda Murphy 00:55:55 Am I up?
DA Dmitrii Anoshin 00:55:59 Hello.
Amanda Murphy 00:56:03 So… We are attempting to add an exporter to hydraulics, and I need a sponsor.
So Hydraulics is a third-party, data… Kind of data lake company?
So… We need, our… the events to be kind of flattened before they are sent to hydraulics.
So I opened up a issue and a… I opened up a full PR, and then changed it back down to a skeleton PR. So I have the skeleton PR up now.
DA Dmitrii Anoshin 00:57:07 Therefore, is this, vendor-specific?
I'm back? Yes.
Okay.
Amanda Murphy 00:57:15 Hydraulics is a… Data Lake Company.
DA Dmitrii Anoshin 00:57:18 Yeah, it's gonna be complicated, I guess, to find a sponsor for Vendor-specific companies these days, given, like, we had the discussion previously about… The focus that we have been doing… I can't focus on trip stabilization and, everything. There is no… just not a kind of capacity. If you have… if you don't have Like, someone from the approvers.
who would be willing to support that, it's probably gonna be challenging to do that. So we typically recommend putting it in a separate build, in your own build on your site in that case.
But if you have some… someone from approvers to… Support that at all. That would work.
Amanda Murphy 00:58:04 Yeah, that's why I'm here, trying to find someone from Approvers.
Alex Boten 00:58:14 One of the… one of the avenues that we've recommended vendors take, more recently has been to do… like, to have an OTLP ingest path.
On the vendor side. Is that something that you've already looked at from that?
Amanda Murphy 00:58:31 Yeah, that's definitely something we've already looked at. We definitely wanna… Kind of force people to use the collector.
So that's part of it.
And then, interested in joining the… Community.
The hotel community.
DA Dmitrii Anoshin 00:58:59 So yeah, for the context, most of the vendors are moving away from their own custom exporters towards OTLP.
And, if you are… You have your own… Format, wire format, right?
and you want to adopt telemetry in general as a project, as an ecosystem, it's better to support OTLP at the backend instead of building collector exporter, because in that case, you'll be able to receive data not only from the collector, but from the instrumentation library and other places.
Amanda Murphy 00:59:34 Yeah, that's… that's what I kind of want to avoid is, collecting data directly from the SDKs, because the way that our database works, it's very, very important to have batching.
Fairly OddParents (ca-wat-brt3) 00:59:49 You can have batching in SDKs, too.
Amanda Murphy 00:59:52 Yeah, but you're gonna have more batching if you have the collector, because you'll be getting it from multiple language agents.
Fairly OddParents (ca-wat-brt3) 01:00:04 Does… does having an OTLP ingestion path Negate your ability to recommend that to people anyway?
Amanda Murphy 01:00:14 No, but it forces it.
DA Dmitrii Anoshin 01:00:19 Also… why that's worth… Make it worse.
Amanda Murphy 01:00:25 It has to do with how the time series database works.
Having… As much in that window, in one payload as possible, is really good.
DA Dmitrii Anoshin 01:00:37 Saying decompression of your protocol is better than a TLP?
Amanda Murphy 01:00:43 preferably better than…
DA Dmitrii Anoshin 01:00:45 compression of your format is better than a GLP.
Or… because you can batch with OTLP and send data over a TLP instead, right?
Amanda Murphy 01:00:57 Well, so, the difference is that when you have the collector, you have multiple language agents all sending data… In one payload?
But if you're sending directly from the SDKs, you have the multiple payloads.
DA Dmitrii Anoshin 01:01:12 But if you send data for the collector and have a TLP ingestion, you can still use a TLP exporter on the collector.
And do the budgeting in the GLP exporter, that's what… All of the… most of the vendors do it, do it.
Fairly OddParents (ca-wat-brt3) 01:01:27 And people using the collector can also make the same mistake as what you're talking about. Like, Collector isn't necessarily only deployed as a gateway that multiple things are sending to. A lot of people will deploy it as a sidecar for every application or something. So, like, you can make the same mistake.
Amanda Murphy 01:01:43 That's true.
Fairly OddParents (ca-wat-brt3) 01:01:44 It's still gonna come down to, like, how you recommend Your customers interact with your stuff, unfortunately.
Amanda Murphy 01:01:52 Yeah.
Fairly OddParents (ca-wat-brt3) 01:01:59 In case it helps, for Google Cloud, we're moving to having an OTLP ingestion route, and we have some documentation for how you can use… basically, you contribute an authentication extension.
for your API, and instruct people to use the OTLP exporter. If you want any resources for how we do that, I can send those along.
Amanda Murphy 01:02:17 Yeah, I worked at New Relic, so, like, we didn't use the collector, we had the endpoint. So, like, I understand how that works.
It's also… we also, like, want to be part of the hotel contrib repo.
But, if… It's impossible to get a sponsor, then.
Pablo Baeyens 01:02:56 So, when you say be part of the… Intrip repo… Do you mean you personally, or… Click Opponent…
Amanda Murphy 01:03:05 the company.
Pablo Baeyens 01:03:08 Oh, Wookie.
Amanda Murphy 01:03:09 I had another engineer from the company here, but he had to leave.
DA Dmitrii Anoshin 01:03:20 Yeah, there are different ways to participate and contribute, rather than introduce a proprietary component, so… Hmm.
Pablo Baeyens 01:03:29 Yeah.
Amanda Murphy 01:03:30 That kind of forces it, though.
Pablo Baeyens 01:03:33 I'd be happy to… well, walk you through the projects that we're working on through DM, if you… if you want to.
But… Yeah, I think what Alex said, before is… the preferred approach, having an OTLP in just, sort of natively in hydraulics.
Amanda Murphy 01:04:09 Yeah, I mean, we definitely weighed those options and decided against that.
For a few reasons.
So you guys aren't accepting any vendor… exporters anymore?
Pablo Baeyens 01:04:34 It is up to the approvers and maintainers whether they want to individually sponsor a component, there's no hard rule about it. We used to have a rule of accepting every vendor-specific component, but we've tried to switch to you should support OTLP natively.
un… We are at time, so, I'm happy to… If you want to open a thread or something on AutoCollector, if you have further questions about how sponsorship works, I'm happy to answer there.
Amanda Murphy 01:05:07 Oh yeah, I have a thread in there already.
Pablo Baeyens 01:05:10 Okay, feel free to ping me on it, If you… if you want my participation. Otherwise, we should call it a day. It's a bit over time.
And if you want to bring this up on a later meeting, that's also okay. Just, I want to be mindful of the time.
DA Dmitrii Anoshin 01:05:37 Thank you, everyone.
Pablo Baeyens 01:05:40 Thank you.
