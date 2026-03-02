SIG: Specification SIG
Date: 2025-09-16
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/gb8tw8QxNlh9YItuAAErv8hUPpGHmLXIluxxtaP64V_kWlM_8SYCFLCetOo81z_4.VllnlrfzcuxCrSSq
============================================================

## Zoom Recording Transcript

**Carlos Alberto Cortez** 00:50 Hello, everybody. Let's start in a couple of minutes.
I only see 6 people now, so yeah. Let's wait. In the meantime, please add your name to the agenda, please, and of course, any important item there can go.
Okay, I guess we can start. It's 3 minutes.
past… sorry, for the… for the voice, what it's called. The first item, trust. You want to share? I can share for you otherwise.
**Trask Stalnaker** 02:30 Would help if I come off mute, wouldn't it?
And maybe turn on my video. Alright.
Yeah, thanks. The first one is just simply a call for…
more reviews. The LogSig has approved it already, and thank you, Josh and Carlos for also approving it.
Probably, would be good to get the… maybe the configuration SIG?
Tyler… I can ping in the configuration SIG Slack…
**Tyler Yahn** 03:15 Yeah, I mean, that's probably a good idea, just to do the Slack, but I could take a look as well.
**Trask Stalnaker** 03:20 Cool. Yeah, that would be great, just since it is kind of crossing, motivated… motivated by
configuration driven. I mean, configuration driven?
Cool.
Any other thoughts?
Questions?
About this…
I think probably with a configuration SIG.
Review, it would probably be good to go.
**Carlos Alberto Cortez** 04:02 Yeah, actually, I was about to merge it, just after I do the specification, but if you want to wait, yeah, probably one review from the config group is enough.
**Trask Stalnaker** 04:13 Yeah, I think that's… yeah, we'll…
We'll wait, I think, if it happens to get in. Are you making the release today?
**Carlos Alberto Cortez** 04:22 Yeah, for this big years, for this month. Okay.
**Trask Stalnaker** 04:24 Cool. Yeah, it doesn't need to be in the release.
All right, next one is something we discussed, yesterday in the semantic convention SIG, and, wanted to bring here, for a more…
General… Discussion… So the idea is… that…
we've had, a lot of PRs into the semantic conventions, adding, like, db.system.name, right? There's, like.
Hundreds of database systems out there. And… We… don't…
really want to, you know, have this list of hundreds of database DB system names, Without…
having, like, those be supported well through the conventions. So, for example, not only… adding the…
enum value, but also explaining, I think, the PR says this…
Yeah, so only define new…
system identifiers when you also document how the conventions apply to that system. For example, when adding a DB system name, also add documentation, like how all the generic attributes apply to that database, since it's, often not
Like, there are specializations needed for each database system.
And I think all of that is fine. The part that is, you know, potentially
Worth getting more eyes on is this statement saying.
Because one of the driving factors that people have submitted these DB system name enum values is because instrumentation is using them.
And so they want it in SEMCOM, so that they can… it can be stabilized, and they can declare instrumentation stable. This is how we've…
This has been the previous expectation, I believe.
And so this is changing it.
To allow instrumentations to use additional attributes as they, not attributes, enum values.
That are not in semantic conventions, and even to stabilize instrumentation, if they choose, that is using enum values that are not in semantic conventions.
Yeah, Josh.
**Josh Suereth** 07:43 Yeah, just to clarify, the enum name would be in semantic interventions.
Some values will be in there, but all enums and semantic conventions are open.
which means people can provide their own value to a needoom. That's, like, an expectation we have on the ecosystem. So, this would let you…
not have the value defined in SumConv, and still be stable. But you can't just invent your own enums, like…
The name, the meaning of the name, all that's still the same.
So, I just want to caveat that.
**Trask Stalnaker** 08:19 Yeah, Daniel.
**Daniel Dyla (Dynatrace)** 08:21 As far as stabilizing instrumentations, does that then assume…
you're using just the standard database conventions, for example, that, like, you know, some databases, like, I don't know.
Redis work differently than MySQL, obviously, and use a different set of attributes, and that's why we've defined specific
SEMCOM for those databases.
In order to stabilize an instrumentation, would you be required to just use the general semantic conventions, or…
Is it… you know… I don't know.
I guess that's the question.
**Trask Stalnaker** 09:02 It's a good question.
**Daniel Dyla (Dynatrace)** 09:06 Okay So this… it's not answered in this, then.
**Trask Stalnaker** 09:16 I think not explicitly, if I had to take a stab at answering that.
I would… Say that the instrument… it's basically giving the instrumentations a little bit more flexibility
So if you were not… if you were building this outside of OpenTelemetry, you were building a… Redis.
Database instrumentation outside of OpenTelemetry.
Right? You could…
do kind of what you want, right? You have the flexibility, you can conform to the general database semantic conventions, you can…
specialize it as to the best of your ability, and use that Redis enum value
There's nothing, and you can declare it stable.
The only thing from a stabilization perspective for external people is following SEM ver, which would be if you then break that, make a breaking change, you would bump the major version.
Inside of OpenTelemetry, we've been more strict.
Saying that it… stable instrumentation must follow stable semantic conventions.
And so, this is kind of creating a little bit of gray area there, but also giving a little bit more flexibility to instrumentations.
To support… those other… enum values.
To the best of their ability.
**Daniel Dyla (Dynatrace)** 10:59 Gotcha. Okay.
Are you not worried about the idea that this might cause…
Different instrumentations to use different enum values for the same database system?
Whether they differ by casing, or hyphen usage, or… Whatever.
**Trask Stalnaker** 11:36 Yeah, that's certainly a concern.
It's… what it's saying… Is, from a receiver perspective, a telemetry consumer perspective.
Is that if the enum value isn't in semantic conventions.
There's no sort of guarantee of consistency.
**Daniel Dyla (Dynatrace)** 12:03 Okay.
**Trask Stalnaker** 12:21 Alright, unfortunately, we don't have, Lenmilla is traveling, So…
Anyway, if you have any further thoughts about it, Please comment on the,
the PR, even if it's just to ask for more clarifications around these sort of… this sort of gray area.
Alright, back to you, Carlos.
**Carlos Alberto Cortez** 12:54 Yeah, thank you so much for that. Yeah, really helpful, Pierre, with the clarification. Let me share now.
Okay, perfect. Yeah, Robert, I think he's applying? Yeah, he's flying.
Okay, let's go over, he has 3 PRs. So this first one is about something we discussed last week.
about, enabled.
And you may remember that, we were discussing about whether, you know, we don't want to make this,
We want to keep it flexible.
And so he changed that to being, like, you know, to be eventually visible when you disable or enable something.
And the important part is this, yes, of course, that it's not necessary for implementations to make sure that changes
Are immediately visible, of colors, but they must be eventually visible.
**Trask Stalnaker** 13:57 My only ask here would be if, we can not merge it for this release, just to give a little bit more time. I started, I'd like to get
the JavaSig eyes on, I was taking a stab at a prototype.
**Carlos Alberto Cortez** 14:18 Since…
**Trask Stalnaker** 14:20 Java doesn't currently follow this.
And so I don't have any… I don't see a… I mean, I agree with this PR, I'd just like to communicate it a little bit more broadly to the JavaSig and have… get some eyes on a prototype.
**Carlos Alberto Cortez** 14:38 Yeah, actually, that's what I wanted to say, that,
I would like to see a prototype of this, you know? I mean, it sounds good, but yeah, I don't think anybody has done that,
And one… at least one prototype would be nice to have.
**Trask Stalnaker** 14:54 I think that Go… I mean, Go is already following this, but I think they're doing it by making it immediately visible.
And so the prototype that I'm going to put up for the Java SIG to discuss on, Thursday's SIG is…
a eventually visible…
**Carlos Alberto Cortez** 15:16 Option. Yeah, yeah, yeah. Makes sense.
Okay, perfect. Yeah, okay.
**Josh Suereth** 15:30 the eventually invisible option in the prototype, we just need to make sure we're testing that on ARM architecture and x86,
Like, just, yeah, just make sure that it's tested on all of them, and then we should be measuring the performance hit.
Of all of the… like, that's… that's the most… like, it's… it's…
A, does it work, because a lot of things that you do that work in x86 will not work in ARM.
and then B, what's our performance hit for making it work?
So, I, I, yeah. Anyway, if you weren't already doing that Trask, let us know. I think we have places we can run ARM tests on?
In our, in our runners, but I might be wrong.
**Trask Stalnaker** 16:15 Yeah, we do… GitHub, has public ARM runners now.
**Josh Suereth** 16:19 Yeah.
**Trask Stalnaker** 16:21 I don't know if we… he…
have them enabled in the Java repo, but I'll check that.
**Carlos Alberto Cortez** 16:36 Perfect.
I hear no more comments on that one, so yeah, thank you so much for that, Trask.
Okay, moving on then, the next one, also from Robert, yeah, I'm extending the attribute.
Types.
wait a second… yeah, you only need reviews, I think.
I don't know, I don't think we have to review this one here.
It's not long, but, yeah, it's…
Probably this is the important part, and there's a discussion here
Another discussion, just a point from Robert. Okay, hadn't seen this.
I remember this one a bit.
I think there are no comments on this one for now. So in that case.
let's review that offline. But yeah, it should be good to go, or just, like, minor clarifications, I think.
Oh, there's a prototype 2.
That's nice.
Okay, I'm hearing silence, so I think that's… yeah, that's the only thing. Just please review that.
And the final one, make configurator optional.
Yeah, I was reviewing this one, and part of the file configuration effort is that there are a pair of components to find there, and this is the configurator and the config ones.
And basically, this is something… yeah, I can show you where this is.
Well, basically, it's how to provide configuration, and it's an abstraction,
It's part of the, value system, sorry, of the… data model.
And basically, Robert was mentioning that they want to make this optional. So, for example, Java already has this, and it's very well defined. But for Go, they don't want to implement this, and just…
Instead, implement the support via processors, which could be an alternative.
Do we have a prototype for this? Tyler, I see that you're online.
**Tyler Yahn** 19:26 Do you mean, like, a prototype for supporting configuration in the GOSIG?
**Carlos Alberto Cortez** 19:30 Yeah, via processors.
**Tyler Yahn** 19:32 Yeah.
**Carlos Alberto Cortez** 19:33 Okay, next.
**Tyler Yahn** 19:36 I mean, yeah, I guess it's a pro-side. It's, like, the using way we implement it in the hotel conf package.
**Trask Stalnaker** 19:49 I would suggest, getting more,
I is from the configuration SIG.
on this, I think, I mean, I think it's fine that…
you know, the important contract is the configuration YAML,
But I know there's some discussions in the configuration SIG around and some spec language.
Around how… discussions around how to customize configuration.
Like, the distro… how distros can… Customize the… whatever YAML was provided.
Just in case there's any future.
Future plans that might rely on having these components?
If that makes sense.
**Carlos Alberto Cortez** 20:51 Yeah, by the way, I would like to… I remember that Yuri wanted these specific components, configurator specifically to exist the way it exists currently, because of potentially remote configuration. So I would like to take some time to dig a little bit to see if I can remember or find where this was defined.
Probably is not required to support remote configuration, like having this configuration… configuration component, but I would like to double check, just in case.
**Josh Suereth** 21:22 Yeah, just to jump in with that,
I don't see the change in this PR, but, like, right above where it makes some things optional, there's a line, for example, for a tracer provider that says, it needs to own the configuration.
should be at the tracer provider level. So, like, if these are implemented as log record processors, I'd like to see your prototype. I think the main concern…
is if, let's say we have OpAmp enabled at some point, right? And we have the ability to push config
After something's created, can you take in that config and update the running of an SDK?
That's a thing that, if we don't support now, we should all anticipate that that is a feature users want. Immediately, as soon as they think of it, right? So we should think of it first.
I… I… like, the idea of using processors to, like, handle that dynamic configuration without having to change the, you know, architecture of how things are wired, I absolutely think that's the right way to go.
Or a… sorry, that is a completely fine way to design this. Like, I'm not trying to say one or the other's better, I think this is totally fine.
My only concern here is to make sure, A, like, the use case is still supported, and B, I don't know if all the parts in the spec are clear.
yet, with this change. Like, we probably need to do…
At least for me to review this, or finish reviewing it, I need to go through it more in depth and find, like, okay.
Here's where you make things optional, but here's where there's confusion caused, because this is not optional, and what does it mean if this statement and that statement aren't true, right?
I think there's a… it…
configuration got really deep into the spec, and I think pulling out and making it optional is gonna be really awkward.
I think that the architecture you propose is totally fine, we just need to sort out the details a bit more. That's all.
**Carlos Alberto Cortez** 23:39 Yeah, that makes sense. Do we have any more comments on that front?
a huge silence, but I think that this is something that we should discuss more.
Maybe not now, but…
Okay, I think that's all for now, so yeah, let's do the reviews. I will take part of this.
On me, that's the end of the agenda.
Do we have anything else?
going twice.
Okay, thank you so much. Yeah, please consider reviewing some of these PRs.
Especially the one regarding, extending the set of attribute value types.
That did reviews. Thank you so much, stay safe, and see you next time.
