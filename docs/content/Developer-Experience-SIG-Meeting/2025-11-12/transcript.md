SIG: Developer Experience SIG Meeting
Date: 2025-11-12
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:16 Hello, hello!
**tristan** 00:17 Hey, hey.
**Juliano Costa | Datadog** 00:19 Good morning.
**tristan** 00:20 The stash, nice.
**Juliano Costa | Datadog** 00:22 It's, Movember, right?
**tristan** 00:25 Yeah.
Oh, is that an international holiday? I didn't know.
**Juliano Costa | Datadog** 00:32 I wouldn't say a holiday, but yeah.
**tristan** 00:36 Yeah, I guess you can have a month-long holiday.
**Juliano Costa | Datadog** 00:42 My wife hates it, so, yeah.
**tristan** 00:44 But, yeah, I… yeah.
every time I grow…
don't shave for a while, and then I do shave. I always leave the stash so that I can walk out and make my wife mad. Then I go back and shave it off, but…
**Juliano Costa | Datadog** 01:02 Hopefully.
**Damien Mathieu** 01:06 Or you should, shave just, like, one side, and then…
**Juliano Costa | Datadog** 01:10 Walk like that.
**tristan** 01:14 Oh, yeah.
**Juliano Costa | Datadog** 01:17 Book.
**tristan** 01:18 I ran out of shaving cream, sorry. I'm just gonna be like this.
**Damien Mathieu** 01:23 I was just asked for, this next Batman movie, for the role of.
**tristan** 01:29 Like, double face?
Yeah, toothpaste, yeah.
**Juliano Costa | Datadog** 01:38 Boop.
**tristan** 01:39 Right.
I'm not sure, sorry, what's his name? The end user SIG.
Canyon.
**Juliano Costa | Datadog** 01:48 10th? Death?
**tristan** 01:50 Ped?
**Damien Mathieu** 01:52 Dan, Dan, Dan. Dan, Daniel. I'm… I would not be surprised if we were at KubeCon.
**tristan** 01:59 Oh…
**Juliano Costa | Datadog** 02:00 Yeah, yeah, true. I think, I think.
**tristan** 02:01 Absolutely.
**Juliano Costa | Datadog** 02:03 to be true, who's that?
Post a picture of the maintainers.
**tristan** 02:10 I could start with, then, just the,
I've reached out to Grok, who…
would be a lot… I actually don't work there anymore. That lasted a month. I don't have…
the capacity to work full-time. I was only working half-time there, and they wanted me to go full-time, and… I can't do that with family issues right now, so…
That sucks, but the… I reached out to the guy I was working with there, and he's…
Brought it up the chain.
And I've… Like, they're… They're really cagey because of the field they're in.
But it's also the… just the OpenTelemetry collection part, so it's like…
**Juliano Costa | Datadog** 02:56 What is their… what is their field? Sorry?
**tristan** 02:59 Oh, yeah, the… so they're in… well, it's the AI field in general, but they also… they make… they… they're in competition with, like, NVIDIA for making chips that do an inference, so it's like…
really… Top secret stuff to them.
**Juliano Costa | Datadog** 03:16 Okay.
**tristan** 03:17 the…
**Juliano Costa | Datadog** 03:17 Nope.
**tristan** 03:18 Yeah, they even have… they have repos you can't even check out. You have to run them in dev VMs in their data centers to, like, work on them. Like, you can't put them on your laptop. They make hardware and stuff like that that they don't want anything getting out. But it's like, come on, it's just the OpenTelemetry collector, how you run that, and…
Collect data, especially… and a lot of the data… well, it is… one of the interesting things about what they do is they have to write…
custom,
receivers and stuff, because they're receiving for their hardware, and, like, all their different pieces, like, PDUs for, like, power… how much power in their data centers is going through, so… some good stuff that would be nice to, like, get out there, and hopefully, maybe they'll eventually open source, and especially if this might push them too, because people might start asking, like, hey, we run data centers too, we'd like to put it through OpenTelemetry. But the…
But yeah, most of the… I mean, the interesting stuff is just how many,
How many clusters they're running.
throughout the world that are running collectors and pushing to central collectors with Arrow, and
they're open about how many data centers they have, not how many are coming online, but how many they have, so I don't think that should be an issue, so I think they'll probably…
come through, and hopefully we can do an interview, like, Friday or something. He's in, Denver, he's in Colorado, so,
Couple hours behind me, so it'd probably be later in the day, but we could see, about making a time that works for everyone, maybe.
**Juliano Costa | Datadog** 04:57 Cool.
But just so I'm… just so I'm not crazy, is this Grok the, like, aluminous Grok, or…
**tristan** 05:06 The what, Greg?
**Juliano Costa | Datadog** 05:08 Isn't Grok a lumbus KI, or X?
**tristan** 05:13 No, no, no, sorry.
**Juliano Costa | Datadog** 05:15 Okay, okay, okay, good, yeah.
**tristan** 05:17 I went over that the first time when I started working there. Maybe I didn't mention I worked there.
And just put it in the document. It's Grok with a Q.
They've…
**Juliano Costa | Datadog** 05:27 Okay, so…
**tristan** 05:29 They've been around for about 10 years, they are soon… Grok with a K.
**Juliano Costa | Datadog** 05:34 Okay.
**tristan** 05:35 For the fact that…
It makes no sense. It's the same thing? They can't use the same name in the same field. They're both in AI.
**Juliano Costa | Datadog** 05:43 Yep.
**tristan** 05:43 Seems like an easy case, but especially when you're going up against a billionaire, it takes…
But yeah, it was a really real problem when I worked there.
**Juliano Costa | Datadog** 05:51 Okay, well.
**tristan** 05:52 And every time I told somebody I worked there, I'd have to go, it's with a Q, it is not the one associated with Iman.
**Juliano Costa | Datadog** 05:58 And I think if you piss, like, Musk, he just buys your company, and then, like, yeah, Dalgrock is mine. I can call it whatever, done.
Beautiful.
**tristan** 06:11 Okay.
**Juliano Costa | Datadog** 06:14 God.
**tristan** 06:15 Yeah. Okay.
**Juliano Costa | Datadog** 06:16 Cool, cool. No, I think, I think it would be a nice, a nice case, mainly because of the…
They're custom components, because I don't think we interviewed anyone with custom components.
**tristan** 06:29 Yep, I don't think so. I feel like maybe Atlassian?
Mentioned one?
**Juliano Costa | Datadog** 06:37 At last time, I think they were using, can't trip everywhere.
**tristan** 06:45 Really?
**Damien Mathieu** 06:47 That's slightly unrelated, and I may not be accepted, but FYI, I have a KubeCon talk scheduled for Amsterdam on using the collector as a framework, and not just something that you use.
And so that's kind of building custom components. So, I don't know, if I do that talk, maybe I… maybe some folks will reach out, who already are doing this.
**tristan** 07:13 In which case, I will definitely bring them up for interviews.
Nice, that's a good idea. Yeah.
**Damien Mathieu** 07:19 I mean, I still have to get accepted.
**tristan** 07:25 We should definitely keep these open, like, the idea, because especially, yeah, I guess the second… agenda item,
This runs into that, in that we shouldn't keep these restricted to, like.
We've got 3, let's stop.
so maybe we shouldn't even… I don't know if we want to reword in the Mastodon posts that we're like, oh, and now coming up is medium, large companies, because we might end up hitting a small company doing something cool with custom components and want to put them in. But the…
the blueprints, I remember Dan had an update about that, but now I thought maybe he'd be here, and he could mention it. Let me check Slack really quick.
I think maybe the update was just asking if we were…
We would be potentially spearheading it, or working in tandem with them.
Because this is our focus, and since this is their focus, I told them this was our focus, so I guess we'll be working in tandem with them,
for… how blueprints go forward, but I don't…
Know any more than that, so hopefully we'll learn more next week about… What they're actually looking to…
I don't know how they're looking to move the project forward.
**Juliano Costa | Datadog** 08:44 Yeah, one thing that, caught my attention there in that thread, was that they want the blueprints to be something kind of live, that people go and update. This was something…
**tristan** 08:58 Oh my god.
**Juliano Costa | Datadog** 08:58 sounded odd. I don't know how they will do that, and, like, what are the intentions of updating?
**tristan** 09:05 Right.
**Juliano Costa | Datadog** 09:06 I mean, of course, the…
the collector deployment evolves as, OpenTelementary matures, and new features come in, and so on and so forth, but yeah.
**tristan** 09:19 Yeah, I wonder if… And I feel like maybe this was…
in the thread, too, that there'd kind of be two components, where we would have these interviews that would be static.
And then the blueprints, which are…
Live. And so, like, you might have a blueprint that matches how a company was doing it, and that might include stuff like the batch processor, because that's what they're using right now, and the interview never changes the blog post about it, but then the… the actual, like, blueprint of…
Now you're starting… your collector configuration would change.
But yeah, I don't know exactly how they plan on doing that, but I think there could be, like, those two components where you can talk to a real live, production use case. I mean, you could also have, not an updated blog post, but, like, a future, like a, let's talk to Atlassian now and see how they're doing it, so…
That is…
**Juliano Costa | Datadog** 10:15 Yup.
**tristan** 10:15 Possibility.
**Juliano Costa | Datadog** 10:18 What has changed the X…
**tristan** 10:20 You're right, because it doesn't…
**Juliano Costa | Datadog** 10:21 Cheers, or, you know.
**tristan** 10:22 some things change… but, like, big things don't change often. So, like, like, if we had done this…
If we had published these, like, a couple months ago, and then wanted… we wouldn't want to suddenly
do a new blog post, because batch processor went away.
Or is deprecated, but we would…
want to do one after, I don't know, a year, or 6 months, or…
When something big changes, but
Yeah. Small changes we don't need to, I don't think.
**Juliano Costa | Datadog** 10:55 I think things will actually change. I don't know if you… if you guys, went through the GC post, recently.
one that Austin, yeah, Austin was writing.
And I think with that, a lot of components will not be on Contrib.
So, the way people are using collectors will change.
**tristan** 11:21 Yeah.
That's… I… One second, let me pull that up. I…
Mmm.
**Damien Mathieu** 11:41 It's not just that a lot of things will not be in country, because if you look at everything, it's also that,
You will be, kind of expected to explicitly say that you want to use components that are unstable.
And so, like, if you build your own collector, I will… you will probably have to enable feature flags for unstable components.
**tristan** 12:06 Will it be… so, like, in configuration… There's, like, a…
I can't remember what it… it's experimental, or it's development, or something, like,
parts of the configuration that are experimental or development have, like, they're, like, slash development in the name? Is it…
**Damien Mathieu** 12:27 I…
**tristan** 12:28 looking at the…
**Damien Mathieu** 12:29 I'm not sure how it's going to be, but what I've read is feature flags. The collector already has a feature flag system. I don't know if it's going to be, like, saying that you want to use unstable components, and then you can use anything unstable, or if it's per component, but it's… I've read feature flags.
I think, like, RFCs are not there yet, anyway, so,
They're probably talking about it this week.
**tristan** 12:56 Okay.
**Juliano Costa | Datadog** 12:59 Yeah.
Yeah.
But, like… If we think about that…
From Datadog's side, 90% of our customers were using Contrib, and from the community side, from the… from the interview that we ran, from the survey that we ran, we saw that 45% of the users were using Contrib.
So, I don't see them migrating to OCB or something, like, a different approach that soon.
**tristan** 13:32 They just have to set a feature flag, then, yeah.
**Juliano Costa | Datadog** 13:35 Well, I'm not sure if that's gonna be the case. I think they will need to set the feature flag, but they will also need to build the…
**tristan** 13:45 Oh.
**Juliano Costa | Datadog** 13:45 To make sure that they import manually the component, because the component will not be part of the distro anymore.
**tristan** 13:51 Gotcha.
**Juliano Costa | Datadog** 13:52 So, yeah, I think this will cause a lot of pain.
**Damien Mathieu** 13:57 Yes, it will.
**Juliano Costa | Datadog** 13:57 community.
**Damien Mathieu** 13:58 It will be both.
**Juliano Costa | Datadog** 13:59 Yep. But, yeah. So, let's see how that develops.
**tristan** 14:05 Yeah.
I like my idea.
just having to put slice development in the config, keep everything in contribute, but then every time they write their config, they have to think about it.
with the…
**Juliano Costa | Datadog** 14:19 Yo.
**tristan** 14:20 the…
And not have just one global flag either, and not make… it would be great if everybody used OCB, but that's gonna be so much pain if everybody suddenly has to.
That'd be interesting, because that would…
Yeah, so that's gonna… I assume that's gonna take a long time, so we definitely… we might want updates once that…
has stabilized, and people have moved to it, and have new blog posts that just… that cover anything that's changed, but just like that, like, hey.
Mastodon, how do you deal with this? Because you are used by third-party people who are running your software, and they can't use Contrib now. They have to build their own collectors. How did you help them do that? Stuff like that.
Yeah, there'll be an interesting case for that.
If they provide anything, they might just say.
Read the hotel docs, but who knows?
So, yeah, hopefully we'll… Talk more about that next week,
On the Mastodon post, I think it's looking good.
Went over it again this morning.
**Juliano Costa | Datadog** 15:46 Yeah, I think we have… I have, two comments, or one comment that I need to actually write, and the others, I'm waiting on team input, so I'll just send a message to the team right now.
**tristan** 16:01 The Macedon team?
**Juliano Costa | Datadog** 16:02 Yep.
**tristan** 16:03 Okay, yeah, I was gonna ask, the main one I was looking at was the, can they share…
Traffic per collector.
**Juliano Costa | Datadog** 16:10 Yeah.
I mean, we do have…
Okay, yeah, we have how many active users they have, and how many nodes, but we do not have the traffic per collector.
**tristan** 16:25 Right.
**Juliano Costa | Datadog** 16:25 I don't know if they have the…
does OTEL… does the collector have any… does the collector have any metric on that?
**tristan** 16:34 Thanks.
**Juliano Costa | Datadog** 16:35 Okay, okay, okay.
**tristan** 16:37 I mean, you can get… you can get, like, how many traces a second, stuff like that.
**Juliano Costa | Datadog** 16:42 But, can we get, like, bytes, or, like, size of the load, or…
**tristan** 16:49 Technically, you can now, I think, but…
**Juliano Costa | Datadog** 16:52 Yes.
Yeah, I hear from big companies, like, hey, we process 1 petabyte of data, and telemetry data. How do they know that?
**tristan** 17:03 Yeah, usually you can look at other, just, like, network in that you're getting from I'm like… the…
Other metrics, like for the container, or whatever you're running.
**Juliano Costa | Datadog** 17:16 Okay, yeah, makes sense. Okay, okay.
**tristan** 17:18 That's what I've done before for the collector. I've just looked at AWS console for, like, how many…
How much network?
**Juliano Costa | Datadog** 17:25 From what you're being.
**tristan** 17:27 What?
**Juliano Costa | Datadog** 17:28 How much we're paying for our income.
**tristan** 17:30 Electronic, yeah.
**Juliano Costa | Datadog** 17:31 Perfect.
**tristan** 17:33 Okay, cool.
Alright, cool, so we've got a couple…
So, we're pretty close with this one, right, you think? And then we can… Send a PR?
Cool.
**Juliano Costa | Datadog** 17:59 Regarding outburst, I'm gonna put the three of us. Should I include team?
**tristan** 18:05 I guess, asking?
**Juliano Costa | Datadog** 18:08 Okay. That's it.
**tristan** 18:09 He's the one being interviewed, so… it's kind of… he's… Then you're gonna…
Either that, or it put in the post.
that you interviewed Tim Campbell, because I don't think that's…
**Juliano Costa | Datadog** 18:25 We, we, we have that.
**tristan** 18:28 I thought you just said Mastodon.
**Juliano Costa | Datadog** 18:30 I think I say Mastodon, but then later on, I have something else.
**tristan** 18:36 Okay.
**Juliano Costa | Datadog** 18:38 Yeah, during the interview, Tim Campbell, and then I have his.
**tristan** 18:43 neither.
**Juliano Costa | Datadog** 18:44 GitHub.
**tristan** 18:47 Yeah, I always forget.
Where do I go to get the recordings for the meetings?
Because they're not, like, public on YouTube anymore, right?
**Juliano Costa | Datadog** 19:00 I think we have all the community… .
**tristan** 19:04 Is it a community repo a link or something?
**Juliano Costa | Datadog** 19:07 Just trying to… together, one sec.
**tristan** 19:14 Not recording… oh, wait, no, this is about governing bodies.
Meeting recordings. Head to meeting… There you go.
Oh, nice, okay, it's populated into a spreadsheet, a giant spreadsheet.
**Juliano Costa | Datadog** 19:29 Yep, yep.
**tristan** 19:30 Nice, thank you.
**Juliano Costa | Datadog** 19:35 No worries.
**tristan** 19:36 Because, yeah, I gotta get the Donst… Don't dangst one written.
And then…
For the next one. I don't know what kind of cadence we're looking for, but, I mean, I'm gonna work on it, as soon as possible. But, yeah, we can obviously not publish it until later, even if it's done.
Maybe, like, once a month or something.
**Juliano Costa | Datadog** 20:05 Well, I don't think we have any…
I don't see as an issue if we publish one today and one another the next week.
**Damien Mathieu** 20:18 I don't see an issue either, but the blog has a lot of blog posts, and they try to keep things, like, something like once a day only.
**tristan** 20:28 They don't probably…
**Damien Mathieu** 20:29 So, yeah.
**tristan** 20:31 Yeah, well, thinking about it, I don't think we need to worry about it, we can just let the…
the natural…
**Juliano Costa | Datadog** 20:37 Posloop?
**tristan** 20:38 it's going through the reviewing and the blog, but yeah, it'll just… it'll work its way out. It's not gonna get…
**Damien Mathieu** 20:45 I agree.
**tristan** 20:47 B.
**Damien Mathieu** 20:47 If we have two posts, like, one every week, that's… In my opinion.
**tristan** 20:54 Cool.
All right.
**Juliano Costa | Datadog** 20:59 I've just pinged Tim from Masuno, so let's see. And I see in the document that, Renault, Reno is on the dock, but I don't know if he's actually looking through. That's the second time I saw him.
**tristan** 21:14 Here.
**Juliano Costa | Datadog** 21:15 So… Yeah, I tied him as optional, because he wasn't part of the interview, but he knows about the
their setup, yeah, so it would be nice to…
I know that he has some stats that he could share, and also how we are presenting or introducing Macedon, he can help with that, so, yeah.
**tristan** 21:40 Nice.
**Juliano Costa | Datadog** 21:42 Cool.
Yeah, I think that's all from… from my… from my side.
**tristan** 21:50 Okay.
**Juliano Costa | Datadog** 21:51 mouse.
**tristan** 21:55 You know, I think it's looking good, close, and I'll get to work on the next blog post.
Before this one gets published, I'm sure, and…
**Juliano Costa | Datadog** 22:06 Club…
**tristan** 22:07 Yeah, hopefully we can get that one out soon, too, and yeah, I'll let you guys know. I should know today, I assume, about whether we could do a Grak, interview on, like, Friday, I'm hoping.
Cool.
Yep.
**Juliano Costa | Datadog** 22:22 Nice. I won't be here next week, I'll be in Paris,
But, yeah, the following one up here, so…
**tristan** 22:32 Alright, yeah, we'll plan…
I plan to still have this meeting, since, hopefully we can talk to Dan, Damian and me, so…
**Juliano Costa | Datadog** 22:42 Cool.
Awesome.
Ben?
**Damien Mathieu** 22:46 Alright, talk to you later.
**tristan** 22:47 Thanks.
**Juliano Costa | Datadog** 22:48 Bye.
