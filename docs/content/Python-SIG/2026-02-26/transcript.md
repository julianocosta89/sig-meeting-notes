SIG: Python SIG
Date: 2026-02-26
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:40 Hello?
**Erdenesaikhan Tserendavga** 01:50 No, we.
**shuwpan** 01:52 Hello!
**Riccardo Magliocchetti** 02:16 Welcome, everyone. We're waiting a few more minutes for more people to join. In the meantime, please add yourself as an attendee to the notes document. And also, if you have any
Topic you want to discuss, feel free to add them as well.
And I shared a link to the notes in the Zoom chat.
**Aaron Abbott** 04:19 Hello, how's it going?
**Tammy Baylis** 04:26 Hi, Erin.
**Riccardo Magliocchetti** 04:51 Okay, I think we can start. So, welcome again to this week's Python Weekly SQL.
If you haven't done it yet, please add yourself as an attendee to the…
SIG, notes document.
And again, if you haven't… if you want to discuss something, please, add any topic, to the list.
That's right.
Okay, so… Let's do this… triage Cool.
**Tammy Baylis** 05:30 Yeah, hi, Ricardo, I… I don't think you were here last week, but yeah, for the last couple meetings, we've, had a lot of PRs, and we wanted to improve, visibility on them. So, I pointed out your board from a while ago, because some of us have still been using it.
De facto.
And since last week, I've, I'm on the approver's list, so every time a PR comes in, I've been trying to categor- at least categorize them better while I do more reviews.
And it was suggested we use the first 5 minutes of the meetings to do triage again. I think we did that in the past, but we just kind of stopped.
So that… yeah, that's a little intro.
State of the Board today, as we can see, the ready for review column is the biggest, with 82.
But I've been trying to focus on the middle three columns, so easy to review, approved PRs that need fixes, approved PRs. I've been looking through conversations on those PRs and, putting them into these columns, so hopefully…
like, easy, approved, that need fix, and approved are the fastest ones we can get merged and going.
that's mainly my report, and yeah, I think the biggest factor is just getting more reviews in.
Yeah, I don't know what else there is to say,
Has anyone else taken a stab at either looking at the board or updating the board this past week?
**Riccardo Magliocchetti** 07:22 Nope, because usually you work faster than me.
And, by the way, thanks for… for doing that. I appreciate it.
**Tammy Baylis** 07:33 Yeah, you're welcome.
**Aaron Abbott** 07:38 Yeah, thank you. And,
That, yeah, that was a good summary. We discussed, kind of, triaging last week, and
you know, ways to kind of scale contributions, and I think
We have a lot… actually, a surprising number of people interested in,
triaging, and then you probably saw, I think it's later in the agenda, but the auto-close PR.
**Riccardo Magliocchetti** 08:02 Yep.
**Aaron Abbott** 08:04 Yeah.
Cool.
**Tammy Baylis** 08:08 Yeah, that's it from me. Please keep reviewing PRs, everyone. Thank you for everything you've done so far, it's been helpful.
**Riccardo Magliocchetti** 08:18 Thank you. Like… My take on this is that I think that…
There are a lot of stuff here ready to review.
What is… Or stale, or… Could be is it too close? Because maybe it's not relevant anymore.
And so… yeah.
**Tammy Baylis** 08:41 Yeah, I found that to be the case also with the column to the left of ready for review. I think it was reviewed and, needs work. If we can go to the left…
Yeah, a lot of these 66 PRs have, not had…
answers on them in a while, so I think maybe the, the stale job
Might close some of them, or mark some of them.
**Riccardo Magliocchetti** 09:30 Yeah, maybe, Lydemira, maybe.
**Liudmila Molkova** 09:35 You just said it.
**Riccardo Magliocchetti** 09:47 Okay, any other comment?
Or…
We can move to the next.
Topic… Nope.
Okay, quick one for me. This, well, this is for my PR by…
I think it's just been updated by Mike.
Yeah.
Like, this is, adding the…
a Basque model based on the CloudyConfig, specification.
And I have a doubt.
Moraquestia?
If, like, of… Where do you think we should put this?
So, is it fine to… for you to add it in the SDK? Or maybe we want a separate, module or package, or…
Whatever, if anyone has opinion.
**Aaron Abbott** 11:00 I mean, I think…
We could start with this, as long as… because it's in the underscore, you know, kind of private namespace, and we could…
Probably move it transparently, right?
**Emídio** 11:18 Yeah, is this being auto-generated, right?
**Riccardo Magliocchetti** 11:23 Yes.
**Emídio** 11:24 You know, so I think if you want to change in the future, it'll be, like, A quick move.
**Riccardo Magliocchetti** 11:37 Okay.
So, like, for me, it's fine as well, but, like, maybe…
Someone has a different opinion, so…
**Aaron Abbott** 11:47 Yeah.
I don't think it's, like, the OpenTelemetry Proto package, where somebody would really want to consume it. For the most part, they…
It's kind of like implementation detail, right?
Maybe that's not true, maybe, like, in, instrumentations?
They might need to access this. That's a good point.
So, like, my understanding of declarative config is you can also have… you can target, you know, certain…
I don't know if we have instrumentation-specific options, but I think you can target them generally. I guess we could also just pass in,
You know, like, dictionary or whatever, but…
for, like, exporters or something like that, or spam processors, I don't know, maybe people would want to use it, but yeah, we could always, revisit it.
**Riccardo Magliocchetti** 12:39 I think that at the moment, the cloud config is specific to the SDK, I think. Like, at least in the docs, it's inside the…
the SDK chapter.
But, yeah, I have to say, like, I want to read this back, so…
Okay.
Next topic is from Mike, but I think he's out of office, so it's not here.
about the, stale… Automation, like, automation for making… Closing…
Like, marketing stale, and then closing, stale PRs.
So… Yeah, I think, there is agreement to merge this.
Anyone else?
Something to add?
Okay.
Everyone is up.
Okay, I'm probably just… I'll approve myself.
Well, maybe the core one maybe needs some…
Like, did we standardize on 40… okay, so it's already up to date. Yeah, should probably merge them then.
Nope.
Okay.
My next topic, also from me, on, yeah, like.
I've started opening PRs for, like, moving the login handler out of the SDK, Into the instrumentation logging,
The logging instrumentation, sorry.
And… Yeah, the first PR… on the SDK side, I only deprecated stuff.
Because I think that we're going to break, like, to remove it when we, move from the underscore logs to…
The logs module when we stabilize the log signal.
So, like, this one is pretty simple, like, the interesting stuff is that,
I found, like, a couple of tests that were, or leaking stuff, or, wrong.
But, like, the functionality was fine.
And on the contrib side, this is, like, a bit more work,
I got a total review from Tammy, thanks.
And so we improved a bit the documentation as well.
So, yeah, like… Looking for approvers?
And I think… Earlier today, or yesterday,
I did with the last bit, because, like, I found that the GenAI examples
We're referencing the hotel Python logging out to instrumentation enabled.
And I think this is because, when this example has been added.
You only had, like, the events, the…
Like, the logger provider, the logger setup, and the event logger.
Set up only when this flag goes on.
And so… yeah. But, like, since at least early 2025, this is not it anymore, and also not sure that…
every, example of a set visc is sending out, logs at all.
So, yeah, like, it should be trivial to approval, but so, like…
An approval from someone, someone that has more.
Like, experience with these, instrumentation would be appreciated.
Okay… yeah, this is just, like, please review, so, like, for me, this is, like, the last thing, we want to be merged before the next release, but it's waiting.
For… More than 2 months, but this is…
a little topic, but Aaron, you… you wanted to say something?
**Aaron Abbott** 18:07 All add a separate vision item.
So, Ricardo, which you want review, is it this one, 4263?
**Riccardo Magliocchetti** 18:33 This is, like, a triple one. I already had a review from the Mila. Okay. The one where I want reviews is the one in the contribib.
Also, like, we added, like, some discussion with Tammy about, like, the user experience, and…
But, like, we improved the documentation, and so should be…
fine, I think. Like, at the moment,
the old code will still continue to work. The user will only see a couple of warnings. One, when a… one from the SDK configuration part.
When they set the… That instrumentation, whatever environment variable, to true.
And the other one from when they instantiate the logging IR class.
from the SDK.
So, like, it's quite maybe annoying, but…
No breakage, at least for the moment.
Okay, speaking of… Like, breakage analysis?
Big time.
**Aaron Abbott** 19:56 Timmy was gonna say something? Sorry.
**Tammy Baylis** 19:58 Oh.
I think
Ricardo, thank you for working on multiple PRs, first of all. Second, I think the other change was, in the docs example of that core PR, where,
Yeah, where's the core PR? Yeah, files changed…
In the example there, is… is that…
There's a… there's an import change
that people need to do. Is that one other change from end… the other change from end usage, or did you mention that already? I wasn't listening too well, sorry.
**Riccardo Magliocchetti** 20:40 like, this one will still continue to work, just with the warnings.
But, like, I just updated the examples so that people will use the…
the one without the barcation, I think.
**Tammy Baylis** 20:56 Right, yeah, okay.
Thank you.
**Riccardo Magliocchetti** 21:19 Okay.
But… well, yeah, I was… as I was saying below, before.
Yeah, we have, like, merged a ton of stuff.
And we haven't released since early December.
So, I was wondering if… It's fine for you if we can…
Once we get this logging and the, deprecation and move.
To cut a new release, even we feel left out.
Something else, and maybe just do, like, a quick,
Release after that, maybe end of March.
Yeah, because, like, I think we are already emerged too many…
changes, I'm a bit scared of.
Any possible regression, or… Feedback we have to handle after that.
So I would like to… Not Adam, even more stuff to care about.
**Aaron Abbott** 22:21 Yeah.
**Riccardo Magliocchetti** 22:22 Like, unless you have something very urgent, or…
**Aaron Abbott** 22:26 Yeah, I had the same feeling, I think we talked about the sampled flag one also.
Last week, the random… it adds a new sampled… sorry, it adds a new bit to the sampled field of trace parent.
I don't know if we merged that one already, but I was…
Thinking the same thing about that one, like, we could save it for the next release if it's not urgent.
Lucas, do you know if we merged that one yet?
No, it's not merged. It's… here, I can… sticker.
Sorry, does it make sense what I'm saying?
**Riccardo Magliocchetti** 23:23 Yep.
For me, yes.
**Aaron Abbott** 23:28 Yeah, and to be clearly, I think I left a comment in here.
You know, if everybody follows the spec, it should be good, but there's probably a lot of code out there that checks if the trace flags equals 1, instead of checking if the
Sampled bit is set.
And…
It might be a little risky of a change, which, you know, obviously people can always downgrade, but since we haven't done a release in a while, it might be nice to do this in a…
Smaller release that's not with so many other changes.
Okay, I mean, if this is urgent, we can… yeah, maybe I'll at least leave a comment on this one. But let me know if it's urgent to get this one in.
**Riccardo Magliocchetti** 24:37 Oh, yeah, you already added it to the… to the notes text.
**Lukas** 24:43 Sorry, I was… I was out for a bit. Are we… are we just planning on… we're just gonna hold off on that, reverse edit?
**Aaron Abbott** 24:52 Yeah, that's what I was suggesting. So, I mean, Lucas, if it's,
Is it urgent to come in this release?
**Lukas** 24:58 I don't… I don't think I even… did I link that? I might have accidentally linked that.
**Aaron Abbott** 25:04 No, no, I added, I added, 48854.
**Lukas** 25:08 Yeah, I guess,
I guess what, yeah, I guess we just need to figure out when we're comfortable with
Letting that go in.
**Aaron Abbott** 25:18 Yeah, I mean, I think the change is fine, it's just, since we haven't done a release in a while.
you know, Just to make it easier for people if they don't have to…
I don't expect any issues, but…
Since it kind of affects, like, other systems, and it's difficult to catch and test, people might have to roll back.
And it would be nice if they don't have to,
lose out on all the development we've done since December, so… Yeah, okay.
**Lukas** 25:44 Yeah, that makes sense.
**Riccardo Magliocchetti** 25:51 Thank you.
And then, like, last one for me, just a quick, for information, but,
virtual environment with Telem21 was released, I think, yesterday, or…
Earlier today, and that broke, touch.
And that broke the… Our generate talks environment.
I had a workaround to stay on all the virtual land?
There is, like, we're working,
Okay, so they fixed that. I don't know if a release is already out.
If a new archae Liz is out, we can drop, they change, but at least…
you know, our CI is green.
Yeah, I'll look at after the…
After the… the call of that.
Okay?
My next topic, Erdin?
Janae, you do this?
**Erdenesaikhan Tserendavga** 27:21 Yeah, hello everyone. Can you hear me?
**Riccardo Magliocchetti** 27:25 Yes?
**Erdenesaikhan Tserendavga** 27:26 Yes.
As we, declared in this,
Semantic conversions, we are proposing the,
Agent types, including the, base agent class, which can, provide,
Create agent type, and, invoke agent types.
Right now,
Some of the frameworks, can provide, remote, grid agent, approach. Most of them, introduce, grid agent.
functionality?
In this, PR… That called, both… approach, which is, client
A remote agent or purchase agent creation.
**Aaron Abbott** 28:26 Do we have an issue for this one? I'm thinking I'm missing a little bit of context.
**Erdenesaikhan Tserendavga** 28:32 Yeah, there is, two different issues for the, different, frameworks, one for the OpenAI agents instrumentation, another one is for AWS Petrock.
**Aaron Abbott** 28:51 Okay,
I can take a look at it, maybe I'm gonna put Keith on the spot, I don't know if you… if you wanna…
Take a look at this one.
**Keith Decker** 29:03 Yeah, I can take a look, too.
**Aaron Abbott** 29:05 Yeah.
**Erdenesaikhan Tserendavga** 29:06 Thank you.
**Aaron Abbott** 29:10 Do you, did you want to, like, say anything about the code, or,
Anything to call out?
**Erdenesaikhan Tserendavga** 29:18 Sure. Right now, I don't have anything, yeah.
**Aaron Abbott** 29:24 Okay, yep, I guess we'll take a look offline. Thank you.
**Erdenesaikhan Tserendavga** 29:29 Thank you.
**Riccardo Magliocchetti** 29:35 Thanks.
Next topic is from Kyiv.
**Keith Decker** 29:42 Sure, so in preparation for, adding the execute tool call, flows through the telemetry handler in GenAI, I'm looking to expand the tool call type to match
Some comps, so that we can be ready for those calls.
The current tool call type looks like it's part of a message part that could be in LLM requests and responses. So, I had to expand that a little bit to get vertex passing, and then expand tool type… tool call type for execute tools.
So I just need some eyes on that. I saw you just commented on that, Aaron, so we can probably talk about that, or unless my intro gives a little bit of a background on that.
**Aaron Abbott** 30:29 Yeah.
I was slightly confused between, which parts are, like, defining the data for the, you know, like, the JSON that gets
I shouldn't say JSON, but the structured data that gets recorded on the spans, and then which part was just kind of like an instrumentation message passing part. Is that…
write kind of what I wrote here, is that accurate?
**Keith Decker** 30:54 Could you expand that on… a little bit.
I'm not following.
**Aaron Abbott** 31:00 This comment here.
**Keith Decker** 31:04 So, so I…
The original types used tool call and then tool call response. I extended that to use tool call request to kind of match that… the message part schema, so that we can use tool call for…
The execute tool.
Spans.
What's up?
**Aaron Abbott** 31:29 So is it, like, a… is it mostly just, like, a rename?
**Keith Decker** 31:33 For the tool call request, it's a rename, and then there's attributes that are coming into tool call.
That, weren't… Necessary for the, message parts.
**Aaron Abbott** 31:47 Okay, I see.
So, a little bit of both, maybe.
**Keith Decker** 31:51 Dear.
Okay. So yeah, I'm trying a PR with just the type changes before we do the handler methods for start and stop tool call.
**Aaron Abbott** 32:03 Okay.
Yeah, I think that was my only feedback, was it was a little bit confusing,
basically just what I said, like, it was a little hard to tell which parts were part of, like, instrumentation getting passed around, and which parts
were, you know, the attributes. So, like, maybe we can use the same one for both,
I think you left… I think Dolan asked a kind of similar question, like, why do we need two things?
**Keith Decker** 32:31 Okay, yeah, when I had just tried to use it with Vertex, it blew up, and I'm not familiar enough with Vertex to…
to see what they're doing there. So I'll go back and look at the unit test that blew up and see.
see if I can make those work.
**Aaron Abbott** 32:49 Was it, like, the test was failing.
Or was it just, like, the assertions were failing?
**Keith Decker** 32:57 The assertions were failing, and it was… I think it was based around that
The new tool called matching the,
The execute tool just added more things than Vertex wants.
I don't know if Vertex was using…
So, I guess I'm not familiar with how Vertex uses message parts here to… to record
tool calls within an LLM call, which is, I think, all that
is part of Vertex Gen AI right now.
So, I guess I just need to explore that a little bit deeper.
**Aaron Abbott** 33:34 Oh, and yeah, I'm also okay with things being separate, if it's kind of clear which parts are…
Part of the, like, structured semantic convention data model, in which parts are just for, like.
Passing around the attributes that would be
recorded on the spin, just part of the instrumentation API, essentially.
And that would be fine to have two parts, in my opinion, but… or, sorry, two different classes, but…
Okay.
Thank you.
**Keith Decker** 34:07 Thank you.
**Riccardo Magliocchetti** 34:11 Thank you.
Next topic is for Tanim.
**Tammy Baylis** 34:19 Yes, hello again. I put in a new PR to replace an old, actually stale PR that I put out, more than a year ago, but yeah, it's,
It should replace a very old issue with the PsychoPG2, instrument connection and uninstrument connection calls, because you can't mutate PsychoPG2 connection objects, so I took Mike's idea, he's not here, but thank you, Mike, for using
a weak ref, weak key dictionary to store, original connections to return them at an instrument. So I got his approval, I got Josh's approval, if I could get,
a green tick approval, that'd be great, because, another fix or feature I'm working on depends on this, which is to, add, SQL commenter support to these functions.
Yeah, please take a look. Thank you.
**Riccardo Magliocchetti** 35:25 Thank you.
So, thank you for your patience.
Okay, next topic… Is Lucas Ayamotakor.
**Lukas** 35:39 Yeah, I just, this has been sitting for…
earlier, like, almost 2 months now, I just…
I know, Ricardo, we tried reaching out to AWS.
And haven't gotten anything.
I think it's pretty well tested.
Yeah, I'm not just not sure if we want to get this in. I know that, at least at my employer, this would be pretty useful to have, but…
**Aaron Abbott** 36:10 So is the issue that we don't have any component owners taking a look?
**Lukas** 36:17 Yeah, I think so.
**Riccardo Magliocchetti** 36:19 Yeah, I tried to reach both of the component owners. One moved from AWS to Microsoft, so it's…
I don't think… Not interested anymore in the… Looking after peace.
**Aaron Abbott** 36:33 And the other one, I cannot…
**Riccardo Magliocchetti** 36:35 find him on Slack, and it doesn't respond to GitHub pings, so… Yeah.
**Aaron Abbott** 36:42 Alright, okay, who wants to… who wants to be a code owner for AIO Photocore?
Anybody interested in this one?
**Lukas** 36:52 I mean, I can be a co-owner, but I'm the one raising the PR.
**Aaron Abbott** 36:57 Yeah, yep.
**Riccardo Magliocchetti** 37:00 like, I think the ministry here is… Do we want to… Like, handle two different packages.
in the same instrumentation or not, like, I think that…
There is a lot of code reusable.
Bah…
Yeah, it's not like one package is a fork of the other, like in the other cases we have.
It's like a research show different?
Maintenance, and so on, but… Yeah, like, probably it's fine.
But I don't… at the moment, I don't have much time to take a look, but…
I think I've said it already before, but I tried to take on it.
**Aaron Abbott** 37:48 Yeah.
I mean, my… I think my recommendation here is somebody can give it, like, a quick
you know, readability kind of review, and, you know, Lucas, I'm sure you tested it, and…
If we don't have converters, we just gotta do the best we can.
**Lukas** 38:05 Yeah, I'm happy… yeah, any feedback is appreciated, and I can do another round of testing if we want to do that. Obviously, there's the…
Testing the repo, but outside of that as well.
**Aaron Abbott** 38:18 Yeah, yeah, and then maybe if, like you, like you mentioned, you're willing to be a co-owner, we could send a follow-up PR to do that, just to…
you know, make sure that this thing is maintained. I think other SIGs are a little more aggressive about removing things that don't have active component owners.
So, it would be helpful if, you know, we should at least keep it up to date, and…
**Lukas** 38:40 Yeah, absolutely. Yeah, it's a… I mean, it's just an extension of BodoCore, so… But yeah, I can definitely be added as a co-owner either way.
**Aaron Abbott** 38:49 Awesome.
Thank you. So, we'll give, like, a quick review and… Not block on the…
On the existing people, if that sounds alright to everyone.
**Riccardo Magliocchetti** 39:12 Next. Oh, thanks, Rufus. Next. Well… Next topic also from you.
**Lukas** 39:18 Yeah.
Yeah, a few questions on this one, I guess. I know this is a pretty large PR, I don't know…
I've tried to…
limited in scope as much as I can, but yeah, this is just, based on some previous discussions for adding OTLP JSON support. This is just the… the ProtoC plugin.
Just wanted maybe an extra set of eyes on it, since it's been…
a little over a week since Annie actually began this. Yeah, I don't know if anything else I want to comment on this.
**Aaron Abbott** 39:57 Yeah, I… I'm interested in this one. I can,
take another pass. Did I leave any… I did leave some comments, right? Are they all…
**Lukas** 40:05 Yeah, I, I addressed it. I think it was… I had a bunch of, kind of, unnecessary helper stuff that I was able to get rid of.
**Aaron Abbott** 40:12 Oh, okay.
Awesome, and do you think it would be helpful, just for review purposes, to split the,
like, the plugin into a separate PR, or if… you could also just split into two commits, or whatever, maybe you've already done that, and then I can just review the…
Oh.
**Lukas** 40:31 Yeah, I can, clean up the… yeah, I can clean up the commits so that the code… I commit the generated code in a separate commit.
**Aaron Abbott** 40:39 Beautiful.
Yeah, basically, just, it'll make it a little easier to,
Figure out what… what to focus on.
**Lukas** 40:47 Yeah, yep.
**Aaron Abbott** 40:49 Cool, and I think some other folks were interested, so, you know, please take a look if you're interested in OTLP JSON.
**Lukas** 41:01 Got it, thanks, yeah.
Yeah, and then this was just the last… just a small one. I think there… I need to probably create some issues here, but…
There are some… I think there are some header casing bugs.
Error.
At least one, if not more, of the… Contrib packages.
Which affects, like, baggage propagation.
So, yeah, just wanted to know, like, what we think… so my approach for solving this was just to add a case-insensitive dictionary to the instrumentation package.
Yeah, just, I could use some extra thoughts or comments on this.
**Aaron Abbott** 41:54 Interesting.
Yeah, I know… I think some… some of the instrumentations rely on the case insensitivity of, like, the…
Whatever the carrier… data class is in the wrapped library to handle this.
So I'm guessing it's kind of… it looks like this one's just scoped to, like, AWS for now, but I think, like.
maybe don't quote me, but I think, like, Flask.
Maybe, actually, now that I'm thinking about it, there was a WSGI…
part of the whiskey spec said to do something with casing. I don't really remember exactly, but yeah, this makes sense to me, and
Yeah.
**Lukas** 42:32 Yeah, I think there's also a bug in Kafka as well, because…
I feel like the… a lot of the HTTP libraries, the headers themselves are already case insensitive dictionaries, so when the carrier or the… yeah, so when the extractor or whatever tries to extract, it's able to actually pull everything out correctly.
**Aaron Abbott** 42:56 Okay, cool. Ricardo, I think you… did you leave comments on this one?
**Riccardo Magliocchetti** 43:04 Yeah, like, I don't know about, like, already under this case, in other record base.
But, like… But yeah, like, I can take another look.
Should be, like, fine.
What can you do, Mila?
Request from green checks, for green checks.
**Liudmila Molkova** 43:36 Yeah, it's been open for a while, and I think it's in a pretty good shape.
And it got through a lot of reviews from… People without green checkmark.
Can he please ask someone to take a look?
Thank you.
**Aaron Abbott** 43:58 Yep.
Yep, we'll do. Thank you.
**Riccardo Magliocchetti** 44:03 Thanks.
And then… Next one from Xuning.
**Shuning Chen** 44:15 Hi, so, yeah, last week I, brought up this PR, so right now it's, ready for review. I already got some comments from
Few people, so I won't get more.
Yeah, comments.
from the community.
So it's for adding an embedding type.
Which, consists with, current SAM conventions.
embedding type.
attributes and,
Yeah, this is only for, spam creation and attributes. Once this got merged, I will add.
metrics and, events.
**Liudmila Molkova** 45:10 Nice, thank you. I'll take a look, and I also will try it out, on OpenAI, because there are embeddings there, and it would be a good testing ground.
I cannot promise to do it today, but by the next call, I should.
**Shuning Chen** 45:25 Yeah, yeah, yeah, sure. Thank you.
**Liudmila Molkova** 45:27 Thank you.
**Riccardo Magliocchetti** 45:31 Thank you both.
And then… Soria?
**Surya Teja** 45:39 Hey, hi. Yeah, this is for, a review on this one. So, Aaron and, Naq took some time to review this and leave some comments, so I…
I've worked… he worked a little bit to refactor this, so if someone can take a look and see if it is looking good, that would be helpful.
**Aaron Abbott** 46:04 Yeah, this is… yeah, I already looked at this one, I can take another look real quick.
**Surya Teja** 46:10 Thanks, guys.
**Riccardo Magliocchetti** 46:17 Thank you.
Okay, this was the last topic for today.
Anyone has something to add?
Otherwise, you have 15 minutes back.
**Liudmila Molkova** 46:40 Thank you.
**Riccardo Magliocchetti** 46:41 Thank you.
**Tammy Baylis** 46:42 Everyone!
**Riccardo Magliocchetti** 46:45 Bye.
