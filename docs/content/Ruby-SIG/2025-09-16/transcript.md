SIG: Ruby SIG
Date: 2025-09-16
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/uaWxHR3YYsaz9PgqJuWnWPgwOX9NKrcmTaAO7MPWRtqoJiI_bwOEgwZVKct32yzq.Yk2deKEHQI2a7THt
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:32 Hello, everyone.
**Hannah Ramadan** 00:36 Thank you, I'm Wendy.
**Wendy Smoak** 00:53 Sorry.
**Kayla Reopelle** 01:22 We'll wait another… Minute, let's see if anyone else joins.
Alright, let's get started.
Okay, Shiden just texted me. He is not feeling well, so he won't be able to join us.
There we go, there's the notes…
Oh, weird, Zoom has, like, presenter layout now? You can have… you could share your screen as your background, or have it over your shoulder, or side by side.
That's kind of… Wild. Alright, we'll try that some other day.
**Hannah Ramadan** 02:46 Over your shoulder, that sounds weird, I don't know the name.
**Kayla Reopelle** 02:48 Yeah, right? I think it was, like, I'm a little in the corner, and, like.
**Hannah Ramadan** 02:53 The screen.
Oh.
**Kayla Reopelle** 02:55 But that was kind of how the diagram was set up.
In the options.
**Hannah Ramadan** 02:59 TikTok vibes.
**Kayla Reopelle** 03:03 Zoom wants to be more like TikTok.
**Hannah Ramadan** 03:06 No crowd.
**Kayla Reopelle** 03:07 Cool.
Okay, so… Let's see, in the spec sig this morning…
There are a few things that I think we'll want to implement and take a look at. None of them, I think, were merged today, so there's still some time. This one for logger, I'm interested in implementing sometime soon. They've now added a minimum, or trying to add a minimum severity feature in a trace-based, logging configuration.
And so, what that would do is that the minimum severity would allow you to only send the log records, hey Daniel, that…
you know, are at that severity or higher, to kind of cut down on what you're interested in, and then I believe the trace-based logger just will send prioritized logs that are connected to traces. And that could also be filtered, I think, by propagator.
So that was the one that felt the most interesting to me.
**Wendy Smoak** 04:14 Need this.
**Kayla Reopelle** 04:15 Oh, good.
**Wendy Smoak** 04:16 And having to filter… I have to filter in the… and I didn't realize it wasn't happening, because it was just, you know, like, you set your whales logger, and it does the thing, and I didn't even think about it, but yeah, everything down to debug was going…
**Kayla Reopelle** 04:27 Mmm…
**Wendy Smoak** 04:28 through the collector, and so the only place I could fix it was to filter in the collector.
**Kayla Reopelle** 04:33 Wow, okay. Well, now we're gonna give an option to filter in the SDK.
**Wendy Smoak** 04:37 Hi.
**Kayla Reopelle** 04:39 So this PR was kind of a discussion about enums and semantic conventions.
And whether, if a convention is an enum, if you need to have approval for every single version of that enum in order for it to be declared, like, a valid convention that could be in a stable instrumentation. So what that looks like in practice is having,
you know, DB system name. That's one of the values that has a ton of different options. You know, the proposal here is to allow, you know, people to put in their own system name here for maybe, like, a niche database that doesn't need a full convention.
I… it seemed like people were interested in approving this, but there was some pushback about, you know, consistency, or what would happen if later on we wanted to make it stable, how would that break things? So, more discussion on that point.
Let's see if the any… any of the other ones…
felt. This one was also kind of interesting. I know we haven't started implementing the configuration…
stuff yet, the file-based configuration, but if we were…
To, this is kind of stating that some or both of the features might be optional to kind of allow
SIGs, if they just want to… the example they gave was if a SIG has not implemented a configurator yet, to allow them to skip that and just go straight into the file-based configuration, option.
So I think more, more will be discussed there later.
The rest of them just kind of felt zoomed through, so I don't really have any extra insights to add beyond the points,
That are on the page.
Any, yeah, any other questions or things that people want to dive deeper into this before we move on?
Okay, cool. I guess we will skip core right now, since there aren't any issues. I, I was…
pulled on to other stuff last week and was out sick for part of it, so I know I have a ton of catching up to do. If there's anything that's really important, please, yeah, add it on here, or let me know about it, but I'm going to focus today on trying to address all the…
open… Questions and changes and such.
Alright, Hannah, you wanna chat about,
This gem and the points that you added.
**Hannah Ramadan** 07:23 Oh, you're muted. Yeah. Yeah, I just wanted to call attention to 3 PRs. This is, following a discussion we had last week of renaming the SQL obfuscation gem to SQL Processor, kind of just to let us put more, like, SQL processing
code into this gem without it having… being so specifically named. These are all in draft right now, only because I just want… I want to do, like, my own review before I officially open them, but they're pretty much ready to go. I plan to open it later.
Today.
The three are introducing the new gem.
adding a deprecation message to the old one, and then switching out the references in the rest of our code. For deprecating the SQL obfuscation gem, I'm not really… I don't know if…
We want to, like, Add a deprecation message, and then keep it around for, like,
Like, I don't really know, I think maybe you just add the message, and then we can delete the code.
From Core… or, sorry, Contrib at some point, but I'm not exactly sure. I didn't find any, like, hotel…
Like…
guidelines for that kind of thing. So, if anyone has any thoughts on that, that would be kind of helpful.
But, like, how… just in case the messages, like, change or anything like that before, so I can, like, make that change now.
**Kayla Reopelle** 08:55 Yeah, I at least haven't been around for any,
any gems being, like, deprecated or removed, that might have happened before I joined the SIG.
And I'm also not aware of anything…
in the specification that would kind of determine how we do that. I know that there are other SIGs. I feel like the collector can trib…
Repository comes to mind, that practice kind of actively deprecating and removing things, so that could be a place to look and see what their systems are.
I think most of the examples That are, like… Ringing bells are,
Things where the maintainers aren't around anymore, rather than kind of, like, renaming something and changing its purpose, but there might still be something there that we could help with, or that could help us.
**Hannah Ramadan** 09:49 Which.
**Wendy Smoak** 09:51 Maybe we need to do one more release?
And, like, so that, you know, you do your bundler upgrade thing that just magically does it, like, so that…
That one can print out stuff and say…
**Kayla Reopelle** 10:02 Yeah.
**Wendy Smoak** 10:02 I'm going away.
**Kayla Reopelle** 10:05 I think that's a great call. Is that what…
I'm going on here right now.
**Hannah Ramadan** 10:10 Exactly, yeah, so in the… I guess in a final release, it would…
Push out, it would all… everything would still work, we would just have a deprecation.
Like, warning.
And then adding notes to the changelog and README pointing to the new.
Gem?
**Kayla Reopelle** 10:28 And then bumping it to a major version, because it's…
**Hannah Ramadan** 10:32 Like, I guess.
**Wendy Smoak** 10:34 Where does it show up, then? Is that those words… is it like a bundler thing when you would try to upgrade, it would print out? Like, I know… I've seen two of your gems are looking for funding, and it, like, prints out right there. Is it something like that we can do, or…
Maybe it just happens magically when you…
**Kayla Reopelle** 10:50 the post-install message, I think that's in the gem spec, and we'd add it there if we wanted to go that approach. But it looks like right now you have a warning message on startup, maybe?
**Hannah Ramadan** 11:00 Yeah, but if there's…
**Wendy Smoak** 11:01 So when you try to configure it, it'll print, it'll print.
**Hannah Ramadan** 11:04 when it, like, loads, this is, yeah. So, but I like the idea of a gem spec type of config message, that seems cleaner.
**Wendy Smoak** 11:14 I don't… and that too, I mean, leave all of them, because you don't know where people are.
**Kayla Reopelle** 11:17 Yeah.
**Wendy Smoak** 11:17 Or even using Bundler, or whatever, so.
**Kayla Reopelle** 11:21 I think.
**Wendy Smoak** 11:22 The more… the noisier it is about what you're trying to… to do, the better chance someone has a chance to see it. And I don't know what's available in the spec.
**Kayla Reopelle** 11:31 Pete, this is it.
Okay, this is like a… this is a global post-install message, so I don't think we want to change that, but, in…
I think it might be set to that constant in here. Yeah, so this is just what you would change, and maybe comment out. Well, I guess we wouldn't need to comment out this line, because it's going away, so we don't need to save the global post-install message for future dates.
**Hannah Ramadan** 11:59 Yeah, we can update it there, and I'll just test it out, see what happens, and maybe share that in the PR.
**Kayla Reopelle** 12:07 Nice.
**Hannah Ramadan** 12:12 Cool, and then ideally, we could just release them one at… like, do them one at a time, just to make sure nothing breaks.
**Kayla Reopelle** 12:20 That sounds good. Yeah, because I think the… the helpers gem is a dependency of all of the database… the SQL database adapters, so it will…
go out to a lot of users, whoever uses Trilogy, MySQL 2, or Postgres instrumentation will get those notifications as well.
Which, maybe it will be good to add something in the message that, like, you know, if you're not installing this gem directly, and you're getting it through this other thing, like.
There's probably a better… there's probably a good way to word this, but, to let people know that no action needs to be taken if
It's coming through those other gems.
**Hannah Ramadan** 13:06 Which is likely the case. Eric did point out last week that it's mostly internally used, so it's.
**Kayla Reopelle** 13:11 Yeah.
**Hannah Ramadan** 13:12 Probably not likely, a lot of people are… Using it directly.
So yeah, that would be a kind of a weird warning for people. It might cause alarm bells.
**Kayla Reopelle** 13:24 Yeah.
**Hannah Ramadan** 13:24 ain't happening.
**Kayla Reopelle** 13:48 Okay, nice.
Yeah, we can…
jump in to these, but I guess before we do that, does anyone else here have any points that they want to discuss?
Okay
So there's a release today. This is something…
I think we need to discuss… I'll be editing this release to hold back the API release for a while. I got some feedback from Francis that,
He would like to find a different way to do a release that isn't a major version bump.
So we're still…
kind of discussing to figure that out, and I think waiting to release the gem until we figure that out is probably the best course of action.
But,
There are some new features and bug fixes, that we should get out for the other gems.
I think there's been some discussion on this one.
This is something that interests you.
adding… Is remote property flags to,
to the exporters. Yeah. So, that's under discussion.
And… Yeah, I think… I mean, there's plenty of stuff here I still need to get caught up myself.
This is a new issue…
Which Robert has assigned himself to, so I don't think…
Has anyone else run into an issue? With this…
I know there was recently an anthropic,
instrumentation that was released, if you are running into this problem, to kind of help pass the context along. So it doesn't emit any new traces, it just helps with the context propagation.
Okay, let's look at contribib… So, new release here… I…
We have the anthropic instrumentation that's gonna get added.
And a release for Docs on Rex instrumentation, so I'll get that going later.
This one…
haven't taken a look at, but if anyone is using Render, it could be a good opportunity to test this out and provide some feedback.
Hannah, are you still working on these? Do you want them to have the keep?
Label on them.
**Hannah Ramadan** 17:09 Yeah, let's have them keep their blocked right now. I don't know if that also could be a label, but…
**Kayla Reopelle** 17:14 I don't know if we have a blocked label, let's see.
We do.
**Hannah Ramadan** 17:18 Oh.
**Kayla Reopelle** 17:27 Nice.
All right, and then issues, do we have any new issues?
We do not.
Okay, well, this might just be a short one today. Is there anything else that people want to discuss?
**Wendy Smoak** 17:54 I'll just chime in on the version number, since I was the one who was…
**Kayla Reopelle** 17:57 Yeah.
**Wendy Smoak** 17:58 being all pedantic about it last time, like, if it's that big of a deal, just go ahead and put a big message in the release notes. I mean, it's not the first project that will have ever broken backwards compatibility in a non-major release.
**Kayla Reopelle** 18:09 Yeah.
**Wendy Smoak** 18:19 Okay, thank you, I appreciate that.
**Kayla Reopelle** 18:23 Yeah, I think communication cycles can just sometimes be slow. It was split a bunch of… across a bunch of different issues, so I still need to just synthesize what the concerns were.
Cool. Okay. Then, if we don't have anything else, I'll let y'all go, and see you next week.
**Wendy Smoak** 18:43 Thanks.
**Hannah Ramadan** 18:44 Thanks, everyone.
**Kayla Reopelle** 18:46 Right?
