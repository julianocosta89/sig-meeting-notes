SIG: PHP SIG
Date: 2025-11-12
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/nLhGqvp5Z8btqXAli_KvUscKBkKOnOT7kC3rHpldbIf_EpcEcwPFBsIAtvM-Q7GL.Lj8BhC1J21Kw1bL0
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:36 Hi, Volt.
**Bob Strecansky** 00:37 Hey, Chris, how are you?
**Chris Lightfoot-Wild** 00:39 Alright, thanks, how are you?
**Bob Strecansky** 00:42 Not too bad, just, going to KubeCon North America today.
**Chris Lightfoot-Wild** 00:48 Very nice.
**Bob Strecansky** 00:49 Yep, Brett got an award yesterday.
**Chris Lightfoot-Wild** 00:52 Breaded.
**Bob Strecansky** 00:53 Yeah, for being an excellent contributor.
**Chris Lightfoot-Wild** 00:56 Nipple.
**Pawel Filipczak** 00:58 insane.
**Chris Lightfoot-Wild** 00:58 Well, amazing.
**Bob Strecansky** 01:01 I think that I nominated him for it, and I don't think that there… I'm assuming that there weren't that many nominations.
Doesn't detract from how awesome of a contributor he is.
**Chris Lightfoot-Wild** 01:14 Did, did he get a paid expenses trip to go and collect the award, or is it just more of an honorary thing?
**Bob Strecansky** 01:21 One more time?
**Chris Lightfoot-Wild** 01:22 Did he get an all-expenses trip to come and collect the award, or…
**Bob Strecansky** 01:26 You know, that would be…
That would be really nice for him, but that's… I mean, that's a pretty long trip.
He has a pretty new… and he has a pretty new baby, so I don't think that would probably work out very well for him. I don't think he'd take it if he got the free trip.
Maybe he would.
They did give us very cool OpenTelemetry maintainer baseball jerseys, which are kind of exciting, but…
**Chris Lightfoot-Wild** 01:50 S.
**Bob Strecansky** 01:51 Beautiful.
I am on my way to the conference, so I will be audio only today. I don't know if anybody has important agenda topics today, but…
Did you want me to do the screen share? If… if you can.
That would be very helpful.
**Chris Lightfoot-Wild** 02:16 Try and declutter my screen somewhat.
If I'll just…
**Bob Strecansky** 02:20 Not sharing… not sharing corporate secrets.
**Chris Lightfoot-Wild** 02:22 It's his personal laptop, so none of those.
**Bob Strecansky** 02:26 No.
I always, yeah, I always, like, I always have a difficult time deciding
like, what I can put on my work laptop and what I cannot.
Always tricky.
**Chris Lightfoot-Wild** 02:40 Well, I prefer… I still prefer Linux, so I've got… personal news, like, on that, and then MacBook for work stuff, so…
**Bob Strecansky** 02:47 Man, we're like birds of a feather, my dude. I'm in the same camp.
**Chris Lightfoot-Wild** 02:52 The only thing I do like on the MacBook is that, you know, the finger unlock kind of.
**Bob Strecansky** 02:56 Oh, yeah, that is pretty sick.
**Chris Lightfoot-Wild** 02:58 That's kind of useful, useful, but other than that…
**Bob Strecansky** 03:03 That's true.
But you also don't have to have a password on your personal machine, which is the best kind.
**Chris Lightfoot-Wild** 03:12 Nice. Excuse me, sorry.
Can we all see the agenda, though?
Unless… probably, Bob, if you're in the car, maybe not, but.
**Bob Strecansky** 03:22 Yeah, I trust that you have it.
Shown.
**Chris Lightfoot-Wild** 03:27 So, today, we're on the 12th…
I don't know why, I think I probably did that last week, but… Useless note.
So there are no, listed agenda topics. Did anyone have anything they wanted to add on before we get going, or,
I guess, add them as well.
Nice. So… I guess we can just start going through.
Open up a bunch of these.
So… pull requests on OpenTelemetry PHP…
A couple of automated ones in there with the, bots.
fighting each other, between Renovate and Dependabot.
Are you still on top of those at the moment, Bob, with.
**Bob Strecansky** 04:48 Yes, yeah, I was… I think we talked about it last week, but we'll continue to do that. I'm just monitoring them. I'll probably, like, converge and merge this week or next. I just wanted to give it a little bit of time to see what the delta was between the two.
**Chris Lightfoot-Wild** 05:07 Boop.
There's a PR here that Neville's waged on, but I guess we can wait for Brett to have you look at that one.
**Bob Strecansky** 05:21 He's… yeah, he's been, I've noticed he's, like, he's been sort of drive-bying, probably when he has a couple free moments, maybe free, and just.
**Chris Lightfoot-Wild** 05:31 Yo.
**Bob Strecansky** 05:31 Viewing slash emerging things, and… I don't think he's doing a lot of active contributing, but he's doing… .
**Chris Lightfoot-Wild** 05:43 Mental.
**Bob Strecansky** 05:44 I like it. If you Slack me that, too, I'm happy to review it to you, Chris.
**Chris Lightfoot-Wild** 05:50 Cool, yeah, can do. Thank you.
**Bob Strecansky** 05:54 Thank you.
**Chris Lightfoot-Wild** 05:55 And then on the list, it's just a bunch of stuff that's already open, mostly for the bot, so… skip that. Just look up PRs, and then come back to the issue board.
After… So, contrary looks like the same, just all, automated PRs.
Wow, 15 in the instrumentation library?
Same story again.
So…
**Bob Strecansky** 06:20 Thank you for your business.
**Chris Lightfoot-Wild** 06:22 He's roughly.
Nothing on Stock Overflow,
So, back to the core report.
**Bob Strecansky** 06:34 So we haven't…
**Chris Lightfoot-Wild** 06:35 Right. Go on.
**Bob Strecansky** 06:38 I was gonna say, I've noticed we haven't had any questions on Stack Overflow in, like, what, about a year? So, I'm wondering if we even have to bother reviewing that anymore. I don't think that anybody's really expecting to field questions there, but that's something we can probably just…
**Chris Lightfoot-Wild** 06:51 I thought you, read my mind the bulk when I was… Oh, really? Oh, really?
**Bob Strecansky** 06:55 Yeah.
**Chris Lightfoot-Wild** 06:56 onto the effort of opening the tab, and there's just never anything there.
**Bob Strecansky** 07:00 I'm going to make an executive decision and say, let's just not stop looking at that in this meeting, and then if we… somebody will raise it with us if they have a problem, I'm certain of it. There's a lot of avenues, and Stack Overflow doesn't have to be one.
**Chris Lightfoot-Wild** 07:13 Yeah, I'd be very surprised if someone went there before Slack, just to try and, you know, get a more immediate response.
**Bob Strecansky** 07:19 or GitHub issues.
**Chris Lightfoot-Wild** 07:21 Dude.
So, okay.
**Bob Strecansky** 07:24 deal. Remove…
**Sergey** 07:25 I was reading that Stack Overflow is losing, kind of, like, popularity, but I wonder what is about to replace it. Reddit? Like, where do people ask questions like that?
They go to repos and open issues.
**Bob Strecansky** 07:39 I… so, I have… and this is a… this is a theory that has no weight behind it, except for my own personal experience. I've noticed that people are getting a lot better at either
opening issues in GitHub repos, I think that process has gotten a lot easier, so I think a lot more people do that now. Or, I think Reddit or AI, I think all, like, the conversions of all of those things has made Stack Overflow a lot less relevant.
Again, personal experience doesn't necessarily mirror what other people think, but that's just how I feel.
**Sergey** 08:13 Hmm.
**Chris Lightfoot-Wild** 08:15 Yeah, I kind of agree with that as well. Especially with the, you know, the accepted answer is usually the thing that an AI would pluck out of the Stack Overflow page anyway.
**Bob Strecansky** 08:25 Right, and… And I think that…
fortunately or unfortunately, I think Reddit also has a lot of AI integration, too, and I think a lot of the selected answers get, you know, reposted to programming questions frequently, and that's another, you know, that's another
Another thing, but anyway. Yeah, I think… good, let's stop reviewing that, stop wasting our time doing that.
**Chris Lightfoot-Wild** 08:49 us.
On the issue board then, there's actually nothing new in here, so it's been a couple of weeks since we've got anything posted. Obviously, there was a question about the way the stack traces are forwarded, which is fairly interesting, but it looks like there's been no traction on that. I think Brett had suggested in that one that…
Yeah, there's not a strong reason for not having this.
**Bob Strecansky** 09:13 Is… is that… is that just an issue that we could just, like… So, help wanted on?
**Chris Lightfoot-Wild** 09:21 Potentially, I guess.
**Bob Strecansky** 09:25 Yeah.
**Chris Lightfoot-Wild** 09:26 I imagine that Brett had said that on here, because it doesn't look like…
**Bob Strecansky** 09:32 I kind of remember seeing something about, like, on those lines too, Chris, but I don't remember where. I agree with you. I remember reading that, and I don't know if we had a discussion… maybe it was a discussion in Slack, or maybe it was… I don't know. We definitely had a discussion about that somewhere. You're not being gaslit by GitHub issues right now.
**Chris Lightfoot-Wild** 09:49 Perfect.
Nice, okay, I'll try and dig that out, and if I can, then we can just label it as Help Wanted, I guess.
**Bob Strecansky** 09:56 Yeah, yeah, I don't know what, like, the correct process for that is. I know that often it might be worth opening a new, like.
Because there's… when somebody opens an issue, and I'd love to hear how other people handle this too, when somebody opens a GitHub issue.
it kind of feels, like, not nice to just go, yep, help wanted. It's almost like you have to process the information in that ticket and open a new issue, but also that's a lot less efficient than just saying, yep, pull request, welcome. I just… I weigh…
Being nice to people and doing extra work.
**Chris Lightfoot-Wild** 10:30 Yeah, I guess it's, like, more of a sort of proper triaging, but, for the extra effort involved.
**Bob Strecansky** 10:37 Yeah, there's definitely extra effort in, like, taking, like, distilling the information from
an issue that somebody creates, and then creating, like, a help-wanted ticket that's associated with the issue. And I also think that that kind of can even get a little bit more complicated, too. So…
you know, oh, I'm tracking this issue.
And there's, like, you know, there's the original issue that got raised, and then there's an issue for the work that's being done on it, and then there's a pull request related to that issue that ties back to the first… you know, it can get… to me, it can just get, like, insanely complicated very quickly. So I'm… again, I'd defer to others if they have a good idea, but…
I almost think that we could say, like, when an issue like that comes in, you can say, like, hey.
You know, if you…
Are you interested in helping with this? If not, we'll open, you know, we can open another ticket.
**Chris Lightfoot-Wild** 11:31 Yeah, no, that sounds good. I'll try and, after this, dig out if I can find what,
Brett's comment, or something related to this, because I'm sure I'd read it, but…
Then, before doing anything on that one is, coin on it now, but… Thank you for that.
**Bob Strecansky** 11:48 works.
**Chris Lightfoot-Wild** 11:49 That's great.
So there was no other issues in there. Obviously, the project board, I guess, is probably as it was last week. Yeah, no updates recently on that side, so the prioritized backlog…
Pretty lean, pending review. Still got my name against that, I should probably try and test that at some point, but…
Yeah, not got around to it, apologies.
I think that's all of the regular, pod. I guess the only question I perhaps had was for yourself, Sergey?
How did you get on from last week's discussion with the, you know, the environment?
**Sergey** 12:33 No, I kind of, like, still, suspended that we needed to finish something, so I don't have, additional feedback, but, yeah, so… but I will get to it maybe next week, so I definitely will, will provide feedback back then.
But, something I wanted to ask you, do you remember there was an issue, this is what I'm currently working on, I wanted to finish that. There was an issue when, OpenTelemeter was loaded in the context of a process that you didn't want it, like Composer, maybe? Or in the context of some FAR file?
Do you remember? Was it Composer?
Oh…
**Chris Lightfoot-Wild** 13:08 Well, I've got a PR for…
**Sergey** 13:11 Okay, so… yeah, this is what I want to do, because currently we are working on something similar. We're trying to… remember, guys, I mentioned that we want to…
Kind of, like, hide all the packages that are being used by, by distribution, so it will not clash with whatever application brings in, the same package, but different versions.
Yeah, including SDK and all that stuff.
Okay, disabled uploading comp… okay, it's in main report.
**Chris Lightfoot-Wild** 13:38 Buried by all of the automatic PRs now.
**Sergey** 13:42 Right, and this is, and how you decided to solve it? By, .
**Chris Lightfoot-Wild** 13:48 So, it checks… and this is a compatibility thing between PSR3 that's bundled into Composer, and then the one that's…
**Sergey** 13:57 Okay, just for me to better understand. Why is it even loaded? How it happened that it loaded in Composer? Because, okay, in Composer, it loads automatically the extension, this I can understand, right?
**Chris Lightfoot-Wild** 14:07 Well, Compose is like a FAR file, isn't it? Like a packaged PHP, so it's got its own internal PSR3.
**Sergey** 14:14 It doesn't load the instrumentation and SDK, because… so it loads automatically the extension.
**Chris Lightfoot-Wild** 14:20 Boom.
Yeah, no, I'm sorry.
**Sergey** 14:23 Yeah, please go ahead. So, what is the… how the PHP code from OpenTelemetry gets into the… into that context?
**Chris Lightfoot-Wild** 14:31 Because when you execute a script, if you, then load in the vendor autoload.
Then it ends up going through the regular process and including all the register files. So the autoload one kicks in for…
**Sergey** 14:46 We're talking about when you have a speech piece scripted in Composer.json?
And you want to execute the script, and the script itself loads the OpenTelemetry?
**Chris Lightfoot-Wild** 14:56 Yeah, that's it.
**Sergey** 14:59 Okay, I see. And the way Composer does it, it loads it in its own context, like, it loads in the same process, and so it clutches with the rest of the loaded packages PHP stuff?
**Chris Lightfoot-Wild** 15:11 Yeah, that's it.
**Sergey** 15:13 So the solution is not to load OpenTelemetry, kind of, like, refuse to load if, it will become, like, no op, if it detects, some contacts or something?
**Chris Lightfoot-Wild** 15:24 Yeah, this is, decides that if it's running in Composer, then it, it won't bootstrap.
Because then it conflicts.
**Sergey** 15:31 I see. But technically, it can happen in any tool that does this kind of trickery, right? That does load some kind of, like, external PHP code that, in turn, can load,
**Chris Lightfoot-Wild** 15:42 Yeah, it could conflict in various ways, I guess. Anive had a suggestion on here as well, so I wasn't sure if…
it was something that, you know, he kind of approved the PR, but I wasn't sure if he wanted to go ahead and make that change or not, but, I don't know if this overlaps with what you were…
Trying to do, though.
**Sergey** 16:02 Yeah, we obviously want to solve it in such a way, because our use case is much wider than that, right? So, it's not limited only to Composer.
it can happen in any application, obviously, if we can clutch with the packages and all the tree that is being brought in because of the SDK, or API, other instrumentations.
So, obviously, if you load those packages automatically, And all the tree.
Then, if we don't do something about it, it might clutch with whatever application brings in, right?
But that's interesting, so it… that means that the composer itself is not protecting itself from this, because,
this step that could have taken by… and I know some tools take this step, like, for example, I understand that PHP standards, like, they tried… whatever they're bringing as dependencies, not their own code, they tried to wrap it into some namespace that will not clash with any code that they can load.
And so this way, they prevent, on their side, any clashes with whatever user code they can load.
**Chris Lightfoot-Wild** 17:07 Good.
**Sergey** 17:08 So, I guess, well, I don't know if Composer will be open to that suggestion or not, but… but currently, I see, so currently that was the solution, just detecting if it's a Composer.
**Chris Lightfoot-Wild** 17:20 Yeah, and maybe that was only for one very niche thing that someone had reported, and then I'd encountered it as well myself, and thought, this is frustrating. That's why I opened this channel.
**Sergey** 17:30 And, and, and it becomes no op in this case? Like, what does it do.
**Chris Lightfoot-Wild** 17:38 Yeah, it essentially negates the SDK being present, so…
**Sergey** 17:45 Huh, okay.
**Chris Lightfoot-Wild** 17:46 So, yeah, no.
**Sergey** 17:47 as if his decay is not present.
**Chris Lightfoot-Wild** 17:49 What was that, sorry?
**Sergey** 17:50 So the effect will be that it's the…
**Chris Lightfoot-Wild** 17:53 Yeah, unfortunately, just because otherwise it blows up anyway with, you get fatal.
So, at least it doesn't blow up around.
**Sergey** 18:04 Just a second.
Excuse me?
Can you repeat that, please?
Some noise here.
**Chris Lightfoot-Wild** 18:16 Yeah, just saying there's a fatal exception, so at least it prevents that from happening, and, you know, the user program can execute as expected, but…
Yeah, but then…
**Sergey** 18:27 I was just wondering, like, can you pretend that this decay is not loaded, or you can, like, switch it as if it's kind of, like, no, this key is loaded, but it just doesn't do anything?
**Chris Lightfoot-Wild** 18:37 Well, look, because the SDK is using the PSR3 for its login, it blows up.
**Sergey** 18:45 Okay, so it all blows up regarding… PSR3, it's about logging.
Okay.
**Chris Lightfoot-Wild** 18:50 I see.
**Sergey** 18:51 And SDK, so you wanted to avoid SDK load in this package that comes with it, like dependency, the PSR dependency?
I see.
**Chris Lightfoot-Wild** 19:01 Yeah, I guess the other thing, and I'm sure Brad suggested this as well, to fix this specific thing would have been… we could make…
the SDK rely on PSR3 by V2 explicitly, rather than V3.
**Sergey** 19:16 This is what Composer depends on, on the tool?
**Chris Lightfoot-Wild** 19:19 Yeah, yeah, but then if you're… obviously, then that could cause conflict with… if you've got an application that you're trying to instrument.
and you're already on V3, and then we come along and say, oh, you have to be on V2.
**Sergey** 19:34 Right, right.
**Chris Lightfoot-Wild** 19:34 That's a point of frustration as well, isn't it, I guess?
**Sergey** 19:37 Yeah, so currently it's flexible, it can load multiple versions depending on what the rest of the constraints are of the application, but if you pin it to V2, then obviously you will, yeah, it will prevent application, like, from being built.
**Chris Lightfoot-Wild** 19:51 So, I mean, realistically, I don't know how common this is for people to run scripts directly from Composer.
**Sergey** 19:58 Right, right.
**Chris Lightfoot-Wild** 19:59 But, I guess… What was that, panel?
**Sergey** 20:04 We use it in our project, kind of, like, but mostly some short things. I don't really see why would you load the SDK in it, right? I agree, but maybe people use it. Well, I guess, yeah, I guess, like, if you use plugin, I guess plugin will also run in that context, right?
And the plugin can be instrumented and want to run, yeah.
**Chris Lightfoot-Wild** 20:27 I couldn't imagine setting up, like, any kind of application to the entry point be Composer, but…
That's not to say someone hasn't done that, and this would cause a problem.
**Sergey** 20:40 Yeah, I mean, yeah, I guess, I can… when we finish with it on our side, we can… we can show and consider. It's gonna be more heavy a solution, and
Obviously, what it tries to achieve is just by… by essentially taking all the packages and their namespaces and hiding them between, behind some, you know, like, top… wrapping it in some kind of top
namespace that will avoid this clash with the… with the normal namespace, right? So it just goes and processes the files textually, just adding and changing the namespace on the top.
Yup. Yup.
And it will only…
be applied to your vendor copy, right? So then you will not clutch. Obviously, it will affect something like SDK, like, if you do have two copies of SDK, they will be two copies, because they will exist in two separate namespaces. So in that case, if you do want to somehow bridge between them, that's an additional task that needs to be considered, but
Putting that aside, most of the packages are not… you don't want that, right? You want them to be completely isolated.
Unless maybe I'm not considering some use case where you do want… it doesn't make sense to isolate it, but anyway, I guess we can revisit. But regarding the configuration, yeah, definitely I'm… it's on my short-term backlog. I will get back to it as soon as possible after we're done with it.
And, then I will have some feedback regarding that.
**Chris Lightfoot-Wild** 22:02 Nice. Thank you.
Cool. Well, if there was nothing else, the only thing I noted as an action was on yourself, Bob, just to, go with that.
decision you made there about removing the Stack Overflow thing, so.
**Bob Strecansky** 22:17 Yep.
Yeah, I also… the only other thing that I want to emphasize is there were a lot of really good talks at KubeCon this week. I think they're all going to get released.
next week on YouTube, so there was a really good one about that roadmap for 2025 to 2026 for OpenTelemetry in general, so…
that would be one that I would encourage people to watch, and there's… there's a bunch of other really good, tech talks, including some ones on OpAmp and a couple other, like, telemetry things, so if y'all need some good…
Some good, car listening, that's a really great thing to do.
**Sergey** 22:55 Oh, that might be interesting. How to find it? Was it, was the op-amp in the name?
Over the top?
Or is it part of the roadmap?
**Bob Strecansky** 23:04 The talks are all on the, they'll all be on the CNCIG, but I'll make sure to link them when they get published. I think that they're gonna publish the… I have a strong suit, and they'll publish them next week.
**Sergey** 23:15 There is already… there is already an agenda available on the internet that.
**Bob Strecansky** 23:19 Yeah, man.
**Sergey** 23:20 Oh, okay.
**Bob Strecansky** 23:20 The conference… the conference is… is this weekend. You can look at all of the talks this week. They won't… probably won't be posted until next week, though.
**Sergey** 23:30 Thank you.
**Bob Strecansky** 23:42 Me.
**Chris Lightfoot-Wild** 23:46 Sorry.
Well… Well, if that's everything, I guess that's the wrap, right?
**Bob Strecansky** 23:58 Thanks, y'all.
**Chris Lightfoot-Wild** 23:59 Enjoy the rest of the conference, Bob.
**Bob Strecansky** 24:04 Will do, thank you. We'll talk to y'all next week.
**Chris Lightfoot-Wild** 24:07 Still.
**Pawel Filipczak** 24:08 Yes.
