SIG: Ruby SIG
Date: 2025-11-04
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZWAHlkHwX9NpB2xnnjZy_LJZoR_nY6yf7EzBWTVWT46EcGIiV_l3OB4rxv2Bm9pe.DJk5gi94e0JuX-rE
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 01:03 Hello, everyone!
Would anyone be willing to share their screen and drive the meeting with the meeting notes today?
**Hannah Ramadan** 01:15 Yeah, I'm happy to do that.
Just need a second to get everything set up.
**Kayla Reopelle** 01:35 Okay, wait, if anyone responded, I don't think I could hear them. Can you guys hear me?
**Wendy Smoak** 01:41 We can hear you. Hannah's doing it.
**Kayla Reopelle** 01:44 Okay, thanks, Hannah.
**Hannah Ramadan** 01:45 Yeah, got it.
Okay, can everyone see my screen? Good?
So… we can start with the spec sig. Was anyone able to go to that?
**Kayla Reopelle** 02:18 I was able to go to part of it. It does seem like there's some bigger discussions going on around maybe a new logging processor.
They also continued some of the conversations from a few weeks ago, related to the four OTEPs, kind of about process and
stabilization of semantic conventions, and kind of like all of those initiatives we mentioned, to give the OpenTelemetry project to its maturity status.
I don't think they're all open yet, but, there's some more things there.
It didn't seem like there was anything that we needed to immediately take action on.
But, but yeah, if you guys see anything in the notes that you want to look at…
Can't take…
**Hannah Ramadan** 03:17 Just looking through, what was that that you mentioned on the semantic conventions front?
I'm looking, I don't… oh, this PR, I think.
Oh, just, okay, refine general event semantics documentation.
**Kayla Reopelle** 03:34 I think that one might have gotten into just, like, a more philosophical conversation about possibly changing what it means to have stable semantic conventions and, how to keep them in
A semantic versioning state and allow instrumentation to stay in that state with maybe having, like, mixed stability?
So I think there was maybe more on that point,
But it's just in the recording.
**Hannah Ramadan** 04:07 Nice, okay, that just seems like a read later kind of thing.
Cool, okay. That looks great for that.
Jumping over into CORE, it looks like, Kayla, you had 3 things.
One open issue… Bumps Symante Conventions version to 137.
**Kayla Reopelle** 04:35 Yeah, there's, there was a problem with Weaver, the tool that we use to auto-generate our code. It was incompatible with some new examples, but, was able to figure that out, so…
Yeah, PR to take a look at at some point. I'll post it in the channel, too.
So that we can get this version out, and then get the next version out that's current.
**Hannah Ramadan** 05:04 Nice, that one looks like a pretty straightforward one.
And then we have, Kayla, a logs release, also.
Oh, it looks like it was already merged, which is great.
**Kayla Reopelle** 05:17 Yes, yeah, thank you so much, Wendy, for opening that PR. I'm sorry for not getting to it until today, but I think…
I left while all the CIs were running, I'm pretty sure they're done now, so I should be able to open up that PR and get the release out in an hour or so.
**Wendy Smoak** 05:34 Thanks, yeah, Arielle was super helpful getting it.
Let's trim down to, just delete some code, better than adding more code. Sorry, I broke it.
**Kayla Reopelle** 05:43 No, it's okay! I mean, I approved the breakage, so no problem.
**Wendy Smoak** 05:49 To be clear, it wasn't broken, it was just very noisy. It was still doing the thing, it was just complaining about stuff it shouldn't have been complaining about.
**Kayla Reopelle** 05:59 Yeah. Thank you, thank you for doing that.
**Hannah Ramadan** 06:10 And then, third on the core, Kayle looks like, asking Schwan if metrics… metrics PR should have been merged.
To initiate a release. We're trying to…
**Kayla Reopelle** 06:21 Yeah, I think the two we merged last week were about, like, views, which there was some logic change that wasn't related to testing.
And I forget what the other one was, but both of their prefixes… one of the prefixes was test, and the other was refactor, so neither initiated a release, so just wanted to check in with you to see if you think that those should be released, too, since I'm going to release locks today.
**Xuan Cao** 06:50 Actually, maybe, well, yeah, you can reduce.
Although, I, I, I kind of answered those,
merge logical also be part of release, but yeah, I think we can release it.
**Kayla Reopelle** 07:16 Okay.
Sounds good.
**Wendy Smoak** 07:18 Kaylee, you just said you're doing a logs release. This is metrics.
**Kayla Reopelle** 07:22 SDK. I can run a release, for both of them, pretty easily with the way our CI is set up. So, yeah, I was just wondering if I should…
Do… do that, or just do the logs?
**Wendy Smoak** 07:40 Well, it says, working on a logs release to address… is 1953 mine, Hannah?
**Kayla Reopelle** 07:45 Yeah.
**Wendy Smoak** 07:45 Yeah, one above.
And it's… it's in Metrics SDK, it's not in Logs at all. So…
**Kayla Reopelle** 07:51 Oh, goodness, okay, I'm sorry. There we go, yep, so it will just…
a metrics SDK with them all. Thank you for catching that.
**Hannah Ramadan** 08:11 Okay, cool, looking at the issues in… Core…
Looks like nothing new has been opened.
Does anyone have anything they want to go over in, core, either in issues or PRs? Let's see…
**Wendy Smoak** 08:38 I had that one about ability to access a
instrument after you create it. I think it's in CORE.
That Kayla commented on.
I did go start a thread in… B… specification channel?
And… Crickets. So, I'm just gonna open an issue over there.
And link it to this one, and just let this one go stale if anyone…
it's not something I have, like.
energy to work on right now. So…
it was just also kind of exploring, how does this community work? Like, if you want to expect change, can you as a normal person get it? And the answer seems to be, well…
Probably not, unless you get someone, like, you know.
a maintainer interested in it to work on. And this one is absolutely not a priority, so…
I did… I did follow up on it, but nothing's happening, so…
**Hannah Ramadan** 09:42 Was that, originally an issue opened in court? I just kind of wanted to take a look.
**Wendy Smoak** 09:47 So, ability to access… that, that one, they're fine. Yeah, you can't… so you create a metrics instrument, and then, like, that's all you can do, create. Nothing else is in the API.
So you can't get it back, you can't remove… and there are other… there's some other conversations going on about being able to remove a metric. So if you create a, observable something.
It's forever. You can't get rid of it.
So there's other, discussions about ability to remove, which…
are kind of similar? Like, how are you gonna remove it unless…
you have to get a… get a hold of it somehow. So…
this exists, and I just wrapped… I mean, I just wrapped the SDK with my own code, so, like, I'm fine, but…
**Hannah Ramadan** 10:37 Yeah, it's…
**Wendy Smoak** 10:37 seems puzzling as a, you know, developer using the SDK, that it just disappears in there, and you can't get it back ever again.
So I see people doing, you know, global constants to point at the metrics instruments, which seems to be…
how one does this, but not what I want to do in my app.
**Kayla Reopelle** 11:03 And remind me, how did you want to access them in your app? Like, what do you think is the… the best path?
**Wendy Smoak** 11:09 I just think the API should have… I mean, it has a create, I just…
**Kayla Reopelle** 11:12 Great.
**Wendy Smoak** 11:12 I should have a find.
**Kayla Reopelle** 11:14 Yeah, yeah.
**Wendy Smoak** 11:15 bad. Seems perfectly logical to me. It doesn't. And it also doesn't have a remove, and, like, there are other… so those discussions are actually kind of more important.
**Kayla Reopelle** 11:25 Okay.
**Wendy Smoak** 11:25 Because you can never get… once you start…
Once you… so if you're using cumulative…
Cardinality, and you create a… sorry, temporality, and you create a thing, and you record it, it's gonna report forever.
There's no way to get… get a hold of it again, and… or get rid of it, so yeah.
**Kayla Reopelle** 11:45 Okay.
**Wendy Smoak** 11:47 So yeah, I'll follow the removal things and see if maybe this happens
As a side effect, and then… other than that, it was just an interesting…
Exploration of what's here, what's possible, how things work around here, who you talk to about what, and all the things, so…
Good stuff, but I did, follow up, but… No progress. Thanks.
**Hannah Ramadan** 12:12 Yeah, it's tough just looking at the PR around, removing instruments. It's been open since 2021. I know! Slash being discussed, but it does look like…
Maybe some recent traffic?
**Wendy Smoak** 12:26 Yeah, last week. Yeah, last… so that's what I was following, the recent discussion about, removal may actually happen.
So, mostly, I need to just…
Find things, write them down, and then wait till someone else gets interested in them, and then tag along behind.
**Kayla Reopelle** 12:44 Yeah, one other thing, too, with this, like, phase and where the POCs are, this person who responded is very active in the SPECSIC. I don't know if he's actually…
A member of the technical committee or not.
But, since there are POCs and there is a spec change.
You said you don't have time for this, but if that changes.
you could add a Ruby POC, and then that would make this more likely to get accepted.
So…
**Wendy Smoak** 13:17 Yeah, that kind of seems like the next thing, open an issue, and then, like, how would you do it, and propose it, because…
**Kayla Reopelle** 13:23 like…
**Wendy Smoak** 13:24 no one else is going to do this. Someone, like, someone has to do the thing to push it forward, and I'm not… I'm not prepared to pick it up right now, this minute, but…
Yes, thank you for helping me.
**Kayla Reopelle** 13:36 See how.
**Wendy Smoak** 13:37 Things work.
**Kayla Reopelle** 13:38 Sorry, it's such a…
**Wendy Smoak** 13:39 Tangled bureaucracy.
Lots of committees, I get it.
**Kayla Reopelle** 13:45 Nope.
**Hannah Ramadan** 13:53 Nice.
Okay, I think that's it for core. Gonna take a look at the contrib issues.
I'm actually just gonna start with PRs, I feel like that's… Anything's new there.
Let's see…
**Kayla Reopelle** 14:14 Like, Ariel's working on… he decided to change… he closed his PR from last week about the HTTP client span names, but since it's in draft mode, it's probably not ready yet.
**Hannah Ramadan** 14:24 Yeah.
**Kayla Reopelle** 14:30 the Other initiative, that we talked a little bit about last week was, trying to get
code owners to be tagged on PRs, and that whole project.
and was able to move forward on that. This PR here, mirrors
a strategy that's used by JavaScript contrib, Python contribib, I think .NET and Java contrib as well. So it seems to be kind of normalizing as the preferred OTEL approach.
For it to fully work, the people who are on this list have to be members of the OpenTelemetry organization. Some of them are, some of them aren't. It should still work, even though they aren't members right now.
And… yeah, so, sent out kind of a list, requesting people to…
apply for membership, and tagged, a few of the maintainers and approvers to make sure that they can, like, second those proposals. So, I personally haven't seen any membership issues open yet, but I am a day behind on my emails.
I think we're safe to merge this in even without those, though, like I said before. Ariel had a few questions about how this would work,
And I… fortunately, the person who created this workflow is very active in OTEL, so he's taking a look at those questions, and expect to hear more soon.
**Hannah Ramadan** 16:12 That's great, I think this is awesome, it's nice to have…
like, people's names and GitHub handles actually tagged and, like, written down, I think that does give some accountability.
Which is great.
Nice.
**Kayla Reopelle** 16:32 We also talked about zero code last week. Was there… I took a look and didn't see anything else I needed to address, personally.
But, schwan, is there anything that you're waiting for on that one? I guess, is it just Ariel?
**Xuan Cao** 16:52 Yeah, and then I saw… and I saw comments. I'll address them, yep.
**Kayla Reopelle** 16:59 Okay.
**Hannah Ramadan** 17:02 Yeah, I took a look too, I thought I looked pretty good, nothing… Like, major from me.
Really exciting to get this merged and out there.
I guess the only other follow-up that I could think of is, like, putting it on the docs site, but that can come later.
**Kayla Reopelle** 17:32 I think there's, yeah, a few other follow-ups, because I think the operator has to release something in their repository, too.
But this is kind of the first domino, I think.
**Hannah Ramadan** 17:44 one, yeah?
Nice work, Sean.
In terms of new contribib issues… just the…
one adding component owners, and then dropping support for Ruby Kafka. I think that's just because it is no longer receiving updates. I think that's great.
**Kayla Reopelle** 18:14 And yeah, and again, kind of in the previous project, JavaScript Contrib had some nice examples for their lifecycle processes. I think they have more process than we do, because they have
a more active… Repository, possibly? But, these are guidelines that we could consider.
Following.
**Hannah Ramadan** 18:44 Yeah, do we have anything written down about…
**Kayla Reopelle** 18:46 No, we don't have anything about, deprecation right now, or removal.
**Hannah Ramadan** 18:55 Yeah, that might be a nice thing to just write down somewhere.
Love that.
Great, I think if there's nothing else, we can move on to burning questions.
**Kayla Reopelle** 19:46 Sounds good.
**Hannah Ramadan** 19:48 Huh?
Schwan, you want to talk about…
How to move the SEMCOM to somewhere that is ready to use.
**Xuan Cao** 19:59 Yeah, so this, SHP metrics, will…
**Hannah Ramadan** 20:05 be used.
**Xuan Cao** 20:06 recording the, HTTP servers and the bind… Duration time?
And, this is just part of a… I think it's part of a step to have, like, the matrix that works on the…
Instrument… instrumentation site, and
is here. I know that those… those are auto-generated, but they're… I mean, if you want… if people want to use it, they have… they have to particularly require this file.
For both Python and JavaScript, they put this, into…
a separate folder, like, for example, in Ruby's, case, it's… it should put it inside the semantic convention folder, so…
My required cards, will just be there.
So I'm just thinking, what is the process, like, moves and…
Because I just, sim- simply…
Create a file, or create the file and folders, or use a process to move this, this kind of a…
SimCon 2.
We're somewhere that's ready to use.
**Kayla Reopelle** 21:30 So, when you're saying use it, like, create the metric, or just use the constant?
**Xuan Cao** 21:36 I'll use a constant.
**Kayla Reopelle** 21:38 So, yeah, so I think the way,
And, yeah, so the way that we're using it right now is that none of… in the new, like, semconf constants, none of them are required straight away, so you do have to require that file.
And then you load only the constants that you want. Oh, but is what you're saying, because the module is just for HTTP and not metrics, you have to…
basically… Are you requiring more?
Are you worried that we're… it's too hard to require them? .
**Xuan Cao** 22:14 I think it's just another step to require, because, for the trace and the resource, you don't need to… you don't need to require…
when you require the OpenTeamergy SDK is automatically in there, but not for this, this… Oh, I see.
**Kayla Reopelle** 22:32 Yeah, yeah, so it was an extra step that, I think was intentional so that
people didn't have everything… all of these constants loaded, if they don't need them. Like, for example, I don't think most people will need the ASPNetCore constants, so I think in the README, there's, like, a suggestion for this approach, for how you can go about it.
But if this doesn't seem…
Like, it's a good option, and we need to, like, restructure it,
We can also take a look at that.
Yeah, thanks for bringing this up, Hannah.
Oh, is that it? Wait, I really thought there was more that got merged.
**Hannah Ramadan** 23:26 Oh no, that's the test. Might be the wrong one, there we go, yeah.
There we go.
**Kayla Reopelle** 23:39 So yeah, I think the other thing, too, was since there's so many, like, incubating unstable constants, that was the other thing. But, so is what you're saying, is it just too cumbersome to do this, to have the require and…
Pull out the constant.
**Xuan Cao** 23:55 Yeah, yeah.
**Kayla Reopelle** 23:56 Okay.
**Hannah Ramadan** 23:57 Yeah.
**Xuan Cao** 23:59 And then, if you look at, the Python.
So they… they put their, like.
I think they move out from this kind of incubating or something like that. They think this is a stable, and then they use it in their WSGI.
Yeah, implementation.
**Kayla Reopelle** 24:20 Okay.
**Xuan Cao** 24:22 Do you have an example for that Python one? I think that would help to take a look.
**Kayla Reopelle** 24:27 Or could you, like, add some links, maybe, to the agenda?
**Xuan Cao** 24:31 Oh, yeah, yeah, sure. I'll do that.
**Kayla Reopelle** 24:37 And then I can… I can take a look at those.
Later, but maybe,
Or, you know, if not, adding them to the agenda, opening an issue so that we can have a discussion on there, because I would like…
Rob Kidd to be part of it, if he is available, since he was kind of redesigning the SEM conference gym.
**Xuan Cao** 24:59 Yeah, I just put in the… as an example.
**Kayla Reopelle** 25:02 Awesome, thank you.
**Xuan Cao** 25:04 And, so, yes, it's a little bit different structure from Python. They only have, Yeah.
Oh, let me just find out the…
**Hannah Ramadan** 25:34 Nice, thanks for writing that link, mate. So, maybe we can…
we could put a post in the Slack channel and tag Rob to kind of
Alert him to this being a discussion. We'd love to have his input on, or just, like, pin this for next time.
Boom.
I don't know when Rob attends, so he might need the Slack channel.
**Kayla Reopelle** 25:58 I think he's usually pretty responsive on Slack.
**Hannah Ramadan** 26:00 Yeah.
**Kayla Reopelle** 26:17 Okay, yeah, sorry to not have an answer here. Would you feel comfortable opening either a GitHub issue or starting a conversation on Slack?
**Xuan Cao** 26:27 Yeah.
**Kayla Reopelle** 26:28 Thanks.
Alright, next one, running…
**Hannah Ramadan** 26:37 Yeah, next one, from also Shawan, introducing runtime metrics.
**Xuan Cao** 26:43 Yeah, so,
I think, they mentioned that there's no missions for Ruby, even though they already have for all other languages, like Python and then…
js, so I think, we can start to introduce, we have to open the issue in OPR, in the semantic convention repository to include those, so…
I'm just… no, I just wanted to check if…
If, like, people are ready to… to,
Do you have this kind of stuff?
**Kayla Reopelle** 27:23 I… I think so. I mean, Wendy, didn't you open… well, I guess it's not really runtime metrics, you were more interested in metrics on the.
**Wendy Smoak** 27:33 Yeah, you opened 1948, I was just opening it to see if this is the same thing. So I was talking about the internal metrics, like, hotel.sdk.processor.log QSize, the metrics about the metrics, and metrics about the, like, the internals. So what is… what are runtime metrics?
**Xuan Cao** 27:53 For Ruby, I'll say mostly just about the coverage collection.
Tas? Some,
And, I mean, you can… I mean, I think the things that people have to have the discussion about, and also agreement on what kind of Ruby metrics should be included in this…
It is, like, inter…
suit of, runtime machines, because, for Python.
something that I think is very important, especially for, say, Python, won't, won't have the same measures in the Node.js as something in Node.js has, Python doesn't have. So, since, just, for Ruby developer, what is most important,
Okay, so the… Dust, yeah.
**Wendy Smoak** 28:43 like, Ruby runtime, like, the…
the language itself, or the… I don't know, are we in a virtual machine? How does this even work?
**Kayla Reopelle** 28:53 Yeah.
Yeah, RubyVM's metrics are something that…
**Wendy Smoak** 29:00 Okay?
Got it.
**Kayla Reopelle** 29:03 Yeah, I think that… That makes sense, if that's an initiative you want to get going.
That would be great.
I think, yeah, we now… I agree that we now have enough of the metrics infrastructure in place in order to do that, and it would probably be…
a metrics, instrumentation and contribib, I imagine? Do you… Sean, is that where you see…
packages for runtime metrics in other languages, or is it usually directly in, like, the SDK?
**Xuan Cao** 29:36 Yeah, that's, that's, so…
The example I, I checked, both Python and JS, they, they only… I think for now, for current progress, they only have this, semantic, semantic convention.
**Kayla Reopelle** 29:51 Right.
**Xuan Cao** 29:52 It's just… it's a… I think they…
Which equipment, what kind of measure they want to include?
They haven't implemented that yet.
**Kayla Reopelle** 30:01 this one.
**Xuan Cao** 30:02 Yeah.
and I think one thing I saw, for the semantic collection, I think we also include
like, other… language semantic information, so I guess that's part of an auto-generation code.
Yeah, yep. So…
**Kayla Reopelle** 30:22 We can't really…
**Xuan Cao** 30:23 we…
**Kayla Reopelle** 30:23 it.
**Xuan Cao** 30:24 Yeah, so… Yeah, we may need to have that.
**Kayla Reopelle** 30:39 Yeah, are you… are you comfortable starting, that work by opening an issue in the semantic conventions repository?
Or… Yeah.
**Xuan Cao** 30:49 Yeah, I… yeah, I, I, and then…
Have all the maintainers to have the discussion about what's… Yeah. Stuff that's most interesting.
**Kayla Reopelle** 30:58 Yep, I think… I think that's a good call.
And yeah, I… we can…
bring some of what we're recording. I know there's also some VM metrics that New Relic hasn't taken a look at, like, related to YJIT, and whether we care about those in OTEL.
**Xuan Cao** 31:20 Hmm.
**Kayla Reopelle** 31:20 We might even want some filters, too, about…
What metrics you… you send or don't send, so…
But I agree, the first step. The first step is the conventions, let's all agree on what… what's standard to collect.
Sweet. Thank you for bringing that up.
**Hannah Ramadan** 31:48 Oh, and the last thing, it looks like Schwann Gen AI Instrumentation.
**Xuan Cao** 31:53 Sorry I had asked too many questions, but, this one…
**Wendy Smoak** 31:59 I'm glad.
**Xuan Cao** 31:59 The two that's.
**Wendy Smoak** 32:00 Wait.
**Hannah Ramadan** 32:01 Great question, yeah.
**Xuan Cao** 32:03 So, yeah, so I saw Python.
They already include all those,
JAI, the actual query spend that is, gonna re… recurrent.
The question user asked, and there's kind of a response.
AI respond?
I think… I think they also… I think this is also kind of a topic in spec… in spec, that they… they already have this stable spec.
**Kayla Reopelle** 32:36 What a kind of.
**Xuan Cao** 32:37 Yeah.
**Kayla Reopelle** 32:38 So I think…
**Xuan Cao** 32:39 maybe we can start to initialize, initialize this kind of a work?
because… because I think it's… AI is gonna be, like, more popular, and people's… all the companies are gonna use their own AI, but eventually they will… all those, popular…
AI endpoint, so…
**Kayla Reopelle** 33:04 Yeah, yeah, I think that's a great idea, and the Gen AI…
Instrumentation is largely related to events, which are logs.
And…
I think the only thing missing there is adding in the event name field, which should be a pretty easy lift.
But, now that, like, OpenAI and Anthropic both have Their own,
gems that are, like, distributed by their companies, I think it's a… it's a nice time to start adding instrumentation.
**Xuan Cao** 33:44 Yeah, if you… I just posted a link, about the GIS, I don't know if you guys look at, so Python has a…
Large.
Well, not large, but they have a, and good.
structure.
**Kayla Reopelle** 34:00 Nice. Which I…
**Xuan Cao** 34:01 Nobody's… yeah.
I'm not sure if JS has this.
**Kayla Reopelle** 34:09 Cool.
**Hannah Ramadan** 34:11 Yeah.
**Kayla Reopelle** 34:15 And what is it? There's a Click House database somewhere that's usually helpful. Well, I guess it's really just a Ruby Gems database. You can use Ruby Toolbox if we want to identify what the most common libraries are. I think Ruby Toolbox just inherits…
or pulls data from RubyGen's downloads to…
**Hannah Ramadan** 34:37 Good.
**Kayla Reopelle** 34:38 content.
Hmm… maybe in categories?
**Hannah Ramadan** 35:02 Hmm.
Could look up, what's the one, like…
**Kayla Reopelle** 35:06 OpenAI, yeah.
**Hannah Ramadan** 35:07 Let's see what…
**Kayla Reopelle** 35:15 Might be root hyphen.
**Hannah Ramadan** 35:23 Hmm, not giving any hints.
**Kayla Reopelle** 35:27 Weird.
Well, okay then. We can look into that differently. Yeah, as far as, like.
instrumentation that already exists. I don't know about the other vendors, but, New Relic does have OpenAI instrumentation through the Ruby OpenAI gem.
And that kind of has an interface for API for a bunch of other languages, or not languages, but,
models, so…
That has been helpful to us, but that was also instrumented before the official, gems came out from the vendors themselves.
**Hannah Ramadan** 36:19 Yeah, it'd definitely be fun to start looking at, more gems and getting instrumentation for it. I really like the way Python has
All of these and the way it's structured.
**Kayla Reopelle** 36:30 Oh, and it does say SEMCOM status is in development. I don't think that needs to stop us, or maybe that's just their SEMCOM status and not the upstream one.
Hmm…
Cool. Those are excellent topics. Thank you for bringing them up.
**Hannah Ramadan** 37:18 Nice, did we have anything else to go over?
Any happy reports?
**Wendy Smoak** 37:25 Just another question… Because Kayla brought up
That, internal metrics thing, so…
OpenTelemetry Weaver is involved here somehow, right? To generate those… that… the code that… that has the constants? Are we using it? I sort of see it in the…
in the repository.
**Kayla Reopelle** 37:48 Yes, the semantic conventions gem uses Weaver to auto-generate the constants in their descriptions that are in the semconf file. The semantic conventions directory is the old stuff that,
We're not gonna break, just because it's in use for people.
**Wendy Smoak** 38:08 Okay, so submit the conventions is… and then some… the shorter one is the one that's generated.
Because over in Python, they're also… Weaver can generate code as well.
**Kayla Reopelle** 38:19 Oh, okay.
**Wendy Smoak** 38:20 And over in Python, they seem to be generating the code to define
So there's a constant that says, you know, that log… that log queue size, whatever one we were talking about, the constant exists, but then there should be a metric, a counter, that…
is going to report that, and so you can generate the code to define the metric.
**Kayla Reopelle** 38:42 Yeah.
**Wendy Smoak** 38:43 and then somewhere else, you have to, like, you know, add to it or something. I don't understand that part yet, but I think the next step might be to…
figure out how Weaver does that, and Python, and make it do it here, too.
**Kayla Reopelle** 38:54 That's really cool.
**Wendy Smoak** 38:56 That's where I was headed. That's why I said I'm not gonna chase down the…
**Kayla Reopelle** 39:00 other things.
**Wendy Smoak** 39:01 Because I'm more interested in that. So I just want to make, like, say those words and see if anyone says, no, that's not how it works at all.
Sound like something possible?
**Kayla Reopelle** 39:12 It does sound like it's something that's possible,
Yeah, I wasn't really exploring the Weaver stuff, Rob was much more immersed in that, and the majority of his work was done over a year ago, so I could have seen the CodeGen stuff maybe coming along afterwards. I know our goal with, like, that first release was to just get back on track with releasing constants.
So I love the idea of code generation as kind of, like, the next phase to actually make those metrics.
**Wendy Smoak** 39:42 Yeah, the next time I have…
time to mess with it, I'll go see what is happening in Python.
**Kayla Reopelle** 39:48 Cool.
**Wendy Smoak** 39:49 And with how they're using it, and maybe get those…
to exist, and then figure out elsewhere. Ariel was talking about, like, totally refactoring everything to have events, and then, like, all that stuff, so I'm definitely not there yet.
Because we need to be able to, like, report how many things are in the queue, how many metrics data points we have, how many…
**Kayla Reopelle** 40:11 Yes, yeah.
Yeah, and I think, you know, those are projects that can evolve over time, too. You know, we can make something that's… that works, and then make something that's…
really great and performant. It's great if you can do them both at the same time, but…
We're an experimental, you know, growing project, so…
**Wendy Smoak** 40:33 Alright, thanks.
**Kayla Reopelle** 40:43 Cool, and then I, had some other stuff come up, so I will have some limited availability this week. I will be back,
full… full-on starting Tuesday, next week. But, I'll keep… I'll keep an eye on things. If anyone…
needs anything really reviewed or attended to today will be the day that I have the most availability.
I'll get that release out. I already opened the PR, so the CI is running.
And, oh, and it looks like everything is passed, so the SDK, the metrics SDK will go out shortly.
**Hannah Ramadan** 41:29 Nice, thank you, Kayla.
**Kayla Reopelle** 41:30 Yeah.
Cool.
**Hannah Ramadan** 41:37 Alright, yep.
**Kayla Reopelle** 41:39 Well, feel free to DM me if there's anything that's, that's urgent.
**Wendy Smoak** 41:45 Thank you.
**Kayla Reopelle** 41:46 Have a great week! Thanks, everyone. Thanks for being flexible.
**Hannah Ramadan** 41:50 experience.
**Xuan Cao** 41:51 Smith.
**Kayla Reopelle** 41:52 I…
