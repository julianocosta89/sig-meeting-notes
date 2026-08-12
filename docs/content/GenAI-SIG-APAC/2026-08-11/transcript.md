SIG: GenAI SIG (APAC)
Date: 2026-08-11
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 00:24 Alan Miller.
Hey, Steve.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 00:28 Hi, folks.
**Trask Stalnaker (Microsoft Corporation)** 00:32 Hey, Huxing Huxing, we finally have the conformance repo!
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 00:42 Oh, is that really? That's really good.
**Trask Stalnaker (Microsoft Corporation)** 00:47 It's not, fully populated yet, but we have it, and we're starting to populate it.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 00:54 Great, great to hear that.
**Liudmila Molkova** 00:59 Trask would you mind driving today? Because I'm on… I have a travel setup.
**Trask Stalnaker (Microsoft Corporation)** 01:06 Yeah, yeah, no problem.
**Liudmila Molkova** 01:07 Thank you.
Okay, I'm on the bust of these guys.
Typically, these variations right here, we have room heater, and then we also have bubble heaters. This is a little bit of a weird thinking, but… the best story.
**Trask Stalnaker (Microsoft Corporation)** 01:36 Alright, let's see, did we have anything…
**Liudmila Molkova** 01:40 Yo.
**Trask Stalnaker (Microsoft Corporation)** 01:40 Yet, nothing yet on the agenda.
**Liudmila Molkova** 01:44 Oh, let's see, no, gotcha.
**Trask Stalnaker (Microsoft Corporation)** 01:46 some neck… okay, these are…
**Liudmila Molkova** 01:48 I think for… generally for…
**Trask Stalnaker (Microsoft Corporation)** 01:51 that other meeting.
**Liudmila Molkova** 01:52 I mean?
**Trask Stalnaker (Microsoft Corporation)** 01:53 Anything that you all wanna…
**Liudmila Molkova** 01:54 This is gonna be crazy. We're getting a lot of backpack.
**Trask Stalnaker (Microsoft Corporation)** 02:05 round.
**Liudmila Molkova** 02:06 from you in Ludmila.
**Trask Stalnaker (Microsoft Corporation)** 02:10 Norse.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 02:15 Let's chat about the repo, and what are we gonna do next? And, how about the blog post?
**Trask Stalnaker (Microsoft Corporation)** 02:26 Yeah.
So, we have… Okay, so we have not landed… we've landed, some of the common infrastructure for running the conformance tests, but we are the first Scenarios are landing… here… And I'm starting to, stack on top of your work, Liudmila, some Java stuff.
**Liudmila Molkova** 03:02 Okay, let's… I… I don't… I will rework this.
There are 23, anyway.
quite a bit, right? I'm not going to address any HTTP, and we'll remove a lot of stuff. So you don't really need to stack on top of Give me a break.
You can just go ahead with yours, and then we'll send another one for GenAI.
**Trask Stalnaker (Microsoft Corporation)** 03:25 Oh, okay. Cool.
Sounds good.
Yeah.
And… So, I would expect we can probably, At least the HTTP ones are pretty… I think straightforward, at least for the sim… I'm just planning to do the simple scenarios, and so… I'd expect to see a lot of those up this week.
I'm gonna tag the language maintainers so that they can, we can pull them into our web.
For… oh yeah, go ahead.
**Liudmila Molkova** 04:10 Do you think we… we should… presented in the spot already. This is a good place to socialize.
**Trask Stalnaker (Microsoft Corporation)** 04:23 Yeah, yeah, yeah, let's at least, you know, drop, the… Like, a teaser.
Of what's happening, and Let people know that we'll be… tagging them. I think the HTTP is a… kind of a… That's actually one of the reasons I want to do the HTTP, is because it's a chance to get all the language maintainers involved.
**For the blog post, Huxing, Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:08 Yes.
**Trask Stalnaker (Microsoft Corporation)** 05:09 Do you… how much… of the instrumentation, like, it… would it make… do you want to… like, I think you could potentially rework the blog post to To point to the work in progress.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:25 Right.
**Trask Stalnaker (Microsoft Corporation)** 05:27 and not necessarily need to, weight.
For all the GenAI scenarios to land.
Or… or you could wait. Like, I think it's… Kind of your choice of the framing and what you want to include there.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:54 I've been… I think I… I can… basically help to, like, promote this project, if there's something that we can share. I think I would prefer there's some… We have a little bit better mature of this repo, and then we can, like.
cross-promote this, I think, with this block.
I think that would be helpful for this project.
So, I would expect there's something that we… we have, at least we should have something in the repo, so I can definitely wait for a moment. I'm not sure… How long will it take, but I can speak.
Maybe we can add some more, like, conformance to… multiple projects.
We can also add our implementations as well.
**Liudmila Molkova** 07:05 Yeah, I'm thinking that the repo currently misses the most important part, which is not even the scenarios, but the dashboard. I think the dashboard will get people very excited in the past.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 07:19 Yes.
**Trask Stalnaker (Microsoft Corporation)** 07:21 Yeah, so let's… let's chat about that briefly, Ludmila.
Because I wasn't sure… whether to… Like, if we're going to eventually… Publish it to the website, or to the ecosystem Explorer.
That's… well, the Ecosystem Explorer is gonna take… probably longer to figure out, although I can ping Jay and kind of see what… Oh.
If he's got ideas for integrating that, and… But that's a little bit more of an explorer, and maybe that's our justification for having it in two places, is… Sort of exploring instrumentation, individually, like, what it does versus… although I guess the Explorer, like, it would be cool to be able to compare instrumentations to each other.
But that's kind of what we want out of the conformance report, is something Maybe that's not necessary. I mean, the report is there, you can still go to the individual instrumentation and see how it's… How it's conforming, and that's probably… Enough, like, it doesn't have to be side-by-side.
**Liudmila Molkova** 08:54 And I'm thinking it might take us a bit of time to come up with the perfect representation.
Right, we will evolve it. Is there anything controversial in just having some form of your dashboard here?
Publishing it, and then, we can… stop hosting it here and move somewhere else. It's unfortunate, but not the end of the world.
**Trask Stalnaker (Microsoft Corporation)** 09:19 Yeah, that's true, we could just redirect.
from that. Yeah.
I like that. Let me… I'll chat with Jake today.
just to kinda… Feel him out on the, ecosystem explorer side… I agree, it would be… Good to… Get the dashboard up in the next, like, 2 weeks, and maybe we… Target that Huxing for your blog post.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 10:01 Cool, that sounds good to me.
**Liudmila Molkova** 10:07 Nice, and then maybe it makes sense to send a PR to Otelio, so we can get the review process started. We'll cover some final details.
And I think it takes, hotel IO people some time to review, so, like, starting in advance would help.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 10:25 Okay, okay, I got it. I would do it, maybe this week, I think.
**Liudmila Molkova** 10:31 Wonderful, thank you.
Do we want scenarios for long suit? Oh, sorry, lungsuit? I'm not sure if I pronounced it right, in this repo.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 10:45 Yeah, I don't… I don't think it's going there, and we can definitely add the… implementations to this repo.
**Liudmila Molkova** 10:57 Okay, so then once we have some of the GenAI populated, I'll ping gear.
And… You would just follow the… Established button.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 11:11 Okay, cool.
Just let me know.
**Liudmila Molkova** 11:13 Yeah, sure. Thanks.
I found a couple of issues with the… this approach.
I'm fixing one in PR number 30.
There are two common components that we reuse across SimConge GenAI.
And this repo.
And these are the… the checkers, like, the… the policies.
And we are currently in a deadlock. So if somebody wants to add something new.
to semantic conventions, GenAI. They either need to Suppress or ignore issues with… Not being conformant.
Or they need to send a PR here, but here we won't take it because it's not in SEMConfire.
And I think I overcame it by just relying on Almost everything from the… Supply registry.
So we, like, in the Rigo policies, for example, we, have had a lot of things hard-coded.
And now they come from the registry.
The final step that people need to apply, so, like, there is this match syntax.
It was used in the past to set expectations and to assert things, and now I… Maybe a little bit, I've used it to provide a spend type here.
So, I'm matching, and then it, gives a spend type. In the future, hopefully spend type lands, and then it can be used as a matcher on its own.
Nice. Yeah.
And then it allows to decouple things.
**Trask Stalnaker (Microsoft Corporation)** 13:17 So, when the run… when we run it in the SEMConf GenAI repo, it'll use the local registry, then… As opposed to right now, it's going through the conformance repo, which is pinned to the released version.
**Liudmila Molkova** 13:36 Okay. Even worse, it's not even Pinter, the released version, the Rigo policies are hard… were hurt with it.
**Trask Stalnaker (Microsoft Corporation)** 13:42 Oh, okay, okay.
**Liudmila Molkova** 13:45 Plus the spend type, like, the reporting based on spend type couldn't work, because you don't know the spend type.
**Trask Stalnaker (Microsoft Corporation)** 13:52 Yeah.
**Liudmila Molkova** 13:55 Yeah.
So, this will probably resolve it. Maybe there are some small issues to solve.
The bigger problem… well, not the bigger, but another problem that I didn't, start thinking about yet is the MOX server.
Is… I have a PR that did something for the usage, and the MOC is not up to date, and now I need to go and update MOC, and it's not a deadlock.
Because I can update MOOC without… like, it's not some conf gap.
But it's just an extra step that would be nice to figure out how to avoid, and, like, if we… maybe I'll just start by updating Mock Server here for now.
But in the long term, if we find it problematic, maybe we'll just split and figure out how to reconcile to different versions.
I don't know, we'll see.
**Trask Stalnaker (Microsoft Corporation)** 14:58 Yeah.
Sounds… either. Yeah, sounds reasonable.
I did want to raise a question, so it kind of come up where the… I think you had brought up the… the… the… a good point about the… reference instrumentations, Sometimes our… problematic… In, that they're not, real instrumentations.
Like, they can't do… like, whether we use monkey patching, or… at some point, I'm wondering… what I'm wondering is.
What, like, long-term… would we… Once we build out more of these instrumentations in the Python GenAI repo.
Just not… would we not need the reference instrumentations and just rely on prototype, or POC, require POC PRs into the Python, or… repo.
directly.
**Liudmila Molkova** 16:13 Just the dog, don't worry.
**Trask Stalnaker (Microsoft Corporation)** 16:16 Yeah, yeah.
And I think the, you know, the reference instrumentation, I think, solves… Right now, helps us because we don't have the coverage in our repo.
And so it kind of gives a cheap way to see across lots of different libraries…
**Liudmila Molkova** 16:47 Yeah.
I… I don't know if coverage is the problem.
So We have instrumentations for… All the scenarios, like, not for every library, but at least one for Every type of the library.
And… It's kind of easy to even scraffold the library.
It's been done to show, like, the feature you're adding as a commit in this.
prototype.
It's just an extra friction point, right, where you need to go to and create the draft pull request, and We can do this, I think what we wanted Is maybe a more strict way to see when people add semantic conventions.
that in the same PR, that there is no instrumentation of any sort, or how this instrumentation would work.
If we say, okay, we just expect a link to POC, then our automated compiler review and us will have a harder time understanding What is this?
**Trask Stalnaker (Microsoft Corporation)** 18:18 So the… I think the Copilot review should be able to do that now, because they actually do an Agentic loop now, as opposed to a static… originally, it was just a static.
review.
So I think it can traverse to that POC.
And validate that way.
Anyway, just wanted to throw it out as, like, I didn't want you to think that I was… only, like, I was insisting on having the reference instrumentations there if there was, if having real prototypes would be useful.
**Liudmila Molkova** 18:59 I mean, it would be useful, like, I think you also see that there, like, despite our efforts, people put hard-coded values and call it…
**Trask Stalnaker (Microsoft Corporation)** 19:10 Yeah, yeah, so that would… Maybe make that… more obvious.
And maybe would make… That clearer to… people. It would also possibly help us push instrumentations forward faster? Like, if for people who want to get land, a semantic invention.
Kind of forces them to write some get a PR up and ready.
**Liudmila Molkova** 19:43 Yeah.
Yes, let's bring it up under… Bigger call? Hmm.
**Trask Stalnaker (Microsoft Corporation)** 19:51 Cool.
**Liudmila Molkova** 19:52 Yeah.
I like it.
**Trask Stalnaker (Microsoft Corporation)** 20:19 Alright, anything else to chat about?
In this meeting.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 20:29 I don't have any topic to discuss right now.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 20:34 Yeah, I don't have, any topic to discard today.
**Trask Stalnaker (Microsoft Corporation)** 20:40 Cool.
Then, to… next week.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 20:45 See you next week.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 20:47 Okay, bye-bye.
**Liudmila Molkova** 20:47 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 20:48 I…
